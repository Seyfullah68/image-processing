import cv2

vid=cv2.VideoCapture(0)# kameradan videoyu aldik

face_cascade=cv2.CascadeClassifier("frontalface.xml")# yuz haar dosyasini import ettik

eye_cascade=cv2.CascadeClassifier("eye.xml")# goz haar dosyasini import ettik

while True: # videolar fotolardan olustugu icin sonsuz while dongusu actik

    ret,frame=vid.read()
    frame=cv2.flip(frame,1)#videoyu y ekseninde cevirdik
    frame=cv2.resize(frame,(480,360))


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# yuzleri bulmak icin gri tonuna cevirdik

    faces=face_cascade.detectMultiScale(gray)# yuzlerin koordinatlarini bulduk

    for (x,y,w,h) in faces:# bulunan koordinatlara dikdortgen cizdik
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    roi_frame=frame[y:y+h,x:x+w]# yuzun bulundugu kismi aldik
    roi_gray=gray[y:y+h,x:x+w]#gri tonda da yuzun bulundugu kismi aldik

    eyes=eye_cascade.detectMultiScale(roi_gray,1.3,4)# gozlerin koordinatlarini bulduk

    for (xx,yy,ww,hh) in eyes:# gozlerin bulundugu koordinatlara dikdortgen cizdik
        cv2.rectangle(roi_frame,(xx,yy),(xx+ww,yy+hh),(0,0,255),2)
    
    cv2.imshow("eyes",frame)

    if cv2.waitKey(5) == 27:
        break

vid.release()
cv2.destroyAllWindows()
