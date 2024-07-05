import cv2
import face_recognition

vid=cv2.VideoCapture(0)# kameradan videoyu okuduk

while True:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)# goruntuyu y ekseninde cevirdik

    faces=face_recognition.face_locations(frame)#yuzlerin koordinatlarini bulduk
    for (y1,x2,y2,x1) in faces:#koordinatlari bulunan siraya gore degiskenlere atadik
        p1=(x1,y1)
        p2=(x2,y2)

        cv2.rectangle(frame,p1,p2,(0,255,0))#koordinatlara dikdortgen cizdik

        cv2.imshow("faces",frame)#ekrana ciktiyi verdik

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
