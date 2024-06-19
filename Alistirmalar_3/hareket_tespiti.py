import cv2

vid=cv2.VideoCapture("body.mp4")

ret,frame1=vid.read() # videonun ilk karesini cektik
ret,frame2=vid.read() # videonun ikinci karesini cektik
while vid.isOpened(): # video devam ettigi surece
    #ret,frame2=vid.read()
    diff=cv2.absdiff(frame1,frame2)#ilk kare ile ikincinin farkini aldik
    cv2.imshow("diff",diff)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)#gri ton a cevirdik

    blur=cv2.GaussianBlur(gray,(5,5),0)#goruntuyu bulaniklastirdik
    cv2.imshow("blur",blur)
    a,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)#treahold uyguladik, siyah ve beyaza cevirdik
    
    dilated=cv2.dilate(thresh,(5,5),iterations=3)#3 kez kalinlastirma uyguladik
    cv2.imshow("dilated",dilated)

    contours,a=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# konturlari bulduk
    cv2.drawContours(frame1,contours,-1,(0,0,255),2)#konturlari cizdik
    cv2.imshow("frame1",frame1)

    frame1=frame2 #framelerin bir sonrakine gecmesi icin
    ret,frame2=vid.read()
    

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()


