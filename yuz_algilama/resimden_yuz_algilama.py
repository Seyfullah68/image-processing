import cv2

img=cv2.imread("face.png") # resmi import ettik

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# haar islemlerini kolay yapmak icin gri ton a cevirdik

face_cascade=cv2.CascadeClassifier("frontalface.xml")# yuz tanima cascade dosyamizi import ettik

faces=face_cascade.detectMultiScale(gray,1.3,5)# yuzlerin koordinatlarini cikardik, 1.3:scale, 5: 5 kere bulununca yuz olarak sayilir

for(x,y,w,h) in faces:# yuz koordinatlarini tek tek aldik, x ve y : baslangic, w:genislik(width), h: yukseklik(heigth)

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)# yuzun koordinatlarina dikdortgen cizdik


cv2.imshow("yuz",img)

cv2.waitKey(0)
cv2.destroyAllWindows()