import cv2
import pytesseract
import imutils
import numpy as np

img= cv2.imread("plate.jpg")#resmi import ettik

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#resmi gri ton a cevirdik
filter=cv2.bilateralFilter(gray,6,250,250)#bu filtre ile resimdeki keskin hatlari yumusattik, degerleri deneme yanilma ile degistirebiliriz
edged=cv2.Canny(filter,30,200)#resimdeki tum koseleri belirledik
contours=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#contourlari bulduk

cnts=imutils.grab_contours(contours)#konturlari bu fonk. ile yakaladik
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]#0 dan 10 a kadar olan konturlarin alanlarina gore tersten siraladik(cunku reverse=true)

screen=None

for c in cnts:
    epsilon=0.018*cv2.arcLength(c,True)#araliksiz olan contourlarin yay uzunlukarini 0.018 ile carparak bu matematiksel degeri bulduk
    approx=cv2.approxPolyDP(c,epsilon,True)#contourlardaki hatayi enaz a indirmek icin yaklasim yaptik
    if len(approx)==4:#eger 4 kose var ise asagidaki islem yapilir
        screen=approx # 4 kosesi olan contour un koordinatlarini aldik
        break

mask=np.zeros(gray.shape,dtype=np.uint8) # maske uygulamak icin resim ile ayni boyutta siyah ekran olusturduk
new_img=cv2.drawContours(mask,[screen],0,(255,255,255),-1)# plakanin oldugu kismi beyaza boyadik
new_img2=cv2.bitwise_and(img,img,mask=mask)# mask ta beyaz olan yeri(plaka) orj img deki yerden aldik

(x,y)=np.where(mask==255)#maskta sadece beyaz olan yerlerin koordinatlarini aldik
(topx,topy)=(np.min(x),np.min(y))#sol ust kosenin koordinatlari
(bottomx,bottomy)=(np.max(x),np.max(y))#sag alt kosenin koordinatlari
plaka=gray[topx:bottomx+1,topy:bottomy+1]#plakayi kirpttik

text=pytesseract.image_to_string(plaka,lang="eng")#plakayi string e cevirdik
print("plakamiz:",text)



cv2.imshow("plate",img)
cv2.imshow("gri",gray)
cv2.imshow("bileteral",filter)
cv2.imshow("canny",edged)
cv2.imshow("mask",mask)
cv2.imshow("new_img",new_img)
cv2.imshow("new_img2",new_img2)
cv2.imshow("plaka",plaka)
cv2.waitKey(0)
cv2.destroyAllWindows()
