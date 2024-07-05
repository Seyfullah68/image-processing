import cv2
import face_recognition

vid=cv2.VideoCapture("faces.mp4") # videoyu okuduk

color=(0,255,0)
while True:
    ret,frame=vid.read()

    face_locations=face_recognition.face_locations(frame)#yuzlerin koordinatlarini bulduk
    for index,locations in enumerate(face_locations):#koordinatlari indexleri ile teker teker aldik
        y1,x2,y2,x1=locations # siralamasina gore koordinatlari degiskenlere atadik

        p1=(x1,y1)
        p2=(x2,y2)

        cv2.rectangle(frame,p1,p2,color) # yuzlere dikdortgen cizdik
        cv2.imshow("face",frame)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.relase()
cv2.destroyAllWindows()


