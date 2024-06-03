import cv2

vid=cv2.VideoCapture("car.mp4") # video yu import ettik

car_cascade=cv2.CascadeClassifier("car.xml")# car detection haar cascade dosyasini import ettik

while 1:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,360)) # videoyu tekrardan boyutlandirdik

    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# gri ton a cevirdik

    cars=car_cascade.detectMultiScale(gri,1.2,2)# arabalarin koordinatlarini aldik

    for (x,y,w,h) in cars:# bulunan koordinatlara dikdortgen cizdik
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("cars",frame)
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
