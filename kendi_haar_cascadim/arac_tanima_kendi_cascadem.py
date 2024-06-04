import cv2

vid=cv2.VideoCapture("car.mp4")# videoyu import ettik

car_cascade=cv2.CascadeClassifier("kendi_car_cascadem.xml")#cascade trainer gui uygulamasinda hazirladigimiz cascade dosyasini import ettik

while True:

    ret,frame=vid.read()#frame leri cektik
    frame=cv2.resize(frame,(640,480))#tekrar boyutlandirdik
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#gri tona cevirdik

    cars=car_cascade.detectMultiScale(gri,1.1,2)#arabalarin koordinatlarini belirledik

    for (x,y,w,h) in cars:# belirlenen koordinatlara dikdortgen cizdik
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("cars",frame)#frame i goruntuledik

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()