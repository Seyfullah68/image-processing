import cv2
import imutils

img=cv2.imread("yaya.jpg") # resmi okuduk

img=imutils.resize(img,250)# resmi tekrardan boyutlandirdik


hog=cv2.HOGDescriptor() # bu fonskiyonu hog degiskenine atadik
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())#yaya algilama islemini bu degiskene. uyguladik

(korninat,a)=hog.detectMultiScale(img,winStride=(4,4),padding=(8,8),scale=1.05)#yayalarin koordinatlarini aldik

print(korninat)


for (x,y,w,h) in korninat:# bulunan koordinatlara dikdortgen cizdik
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()