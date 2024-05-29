import cv2

vid=cv2.VideoCapture("faces.mp4") # videoyu import ettik

face_cascade=cv2.CascadeClassifier("frontalface.xml")# yuz tanima haar cascade yi import ettik

while True:

    ret,frame=vid.read()# video yu okuduk

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# frameleri gri ton a cevirdik

    faces=face_cascade.detectMultiScale(gray,1.3,4) # yuzlerin koordinatlarini bulduk

    for(x,y,w,h) in faces: # yuzlerin koordinatlarinin baslangic, genislik ve yukseklik degerlerini bulduk

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)# bulunan degerlere dikdortgen cizdik
    
    cv2.imshow("faces",frame)# frame i gosterdik

    if cv2.waitKey(5) == 27:
        break

vid.release()
cv2.destroyAllWindows()


