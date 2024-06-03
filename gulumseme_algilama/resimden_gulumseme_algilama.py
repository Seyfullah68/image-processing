import cv2

img=cv2.imread("smile.jpg")

face_cascade=cv2.CascadeClassifier("frontalface.xml")#haar cascade yuz tanima dosyasini import ettik
smile_cascade=cv2.CascadeClassifier("smile.xml")#haar cascade smile tanima dosyasini import ettik

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#gorseli gri ton a cevirdik

faces=face_cascade.detectMultiScale(gri,1.3,4)#yuzlerin koordinatlarini bulduk
for (x,y,w,h) in faces:#bulunan koordinatlara dikdirtgen cizdik
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

roi_smile=img[y:y+h,x:x+w]#yuzun bulundugu kismi belirledik
roi_gri=gri[y:y+h,x:x+w]

smiles=smile_cascade.detectMultiScale(roi_gri,1.3,4)#belirlenen kisimda smile larin koordinatlarini bulduk
for (xx,yy,ww,hh) in smiles:#bulunan koordinatlara dikdortgen cizdik
    cv2.rectangle(roi_smile,(xx,yy),(xx+ww,yy+hh),(255,0,0),2)

cv2.imshow("smile",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
