import cv2 

img=cv2.imread("eye.png") # fotoyu import ettik

face_cascade=cv2.CascadeClassifier("frontalface.xml")# yuz algilama haar dosyasini import ettik

eye_cascade=cv2.CascadeClassifier("eye.xml")# goz algilama haar dosyasini import ettik

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# resmi gri ton a cevirdik

faces=face_cascade.detectMultiScale(gray,1.3,5)# gri tondaki resimde yuzlerin koordinatlarini belirledik

for (x,y,w,h) in faces:#belirlenen koord. dikdortgen cizdik.x ve y: baslangic, w: genislik, h:yukseklik
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

img2=img[y:y+h,x:x+w]# resimde yuzun oldugu kismi aldik
gray2=gray[y:y+h,x:x+w]# gri tonda da yuzun oldugu kismi aldik

eyes=eye_cascade.detectMultiScale(gray2)# alinan gri kisimda bulunan gozlerin koord. larini tespit ettik

for (xx,yy,ww,hh) in eyes:# gozlerin koordinatlarina dikdortgen cizdik
    cv2.rectangle(img2,(xx,yy),(xx+ww,yy+hh),(255,0,0),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()