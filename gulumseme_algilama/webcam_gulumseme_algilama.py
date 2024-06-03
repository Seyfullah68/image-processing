import cv2

vid=cv2.VideoCapture(0) # videoyu cameradan aldik

face_cascade=cv2.CascadeClassifier("frontalface.xml")# yuz tanima cascade haar dosyasini import ettik
smile_cascade=cv2.CascadeClassifier("smile.xml")# smile tanima cascade haar dosyasini import ettik

while 1:
    ret,frame=vid.read()#videodan frame i cektik
    #frame=cv2.resize(frame,(640,380))#gorseli yeniden boyutlandirdik
    frame=cv2.flip(frame,1)#gorseli y ekseninde cevirdik
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#gri ton a cevirdik
    faces=face_cascade.detectMultiScale(gri,1.5,9)#yuzlerin koordinatlarini bulduk
    for (x,y,w,h) in faces:#bulunan koordinatlara dikdortgen cizdik
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,2550),3)
    
    roi_smile=frame[y:y+h,x:x+w]#yuzlerin bulundugu yeri ayri bir degiskende tuttuk.
    roi_gri=gri[y:y+h,x:x+w]

    smiles=smile_cascade.detectMultiScale(roi_gri,1.5,9)#gulumsemelerin koordinatlarini bulduk
    for (xx,yy,ww,hh) in smiles:#bulunan koordinatlara dikdortgen cizdik
        cv2.rectangle(roi_smile,(xx,yy),(xx+ww,yy+hh),(255,0,0),2)
    
    cv2.imshow("smiles",frame)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()