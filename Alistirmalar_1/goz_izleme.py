import cv2

vid=cv2.VideoCapture("eye_motion.mp4")

while True:
    ret,frame=vid.read()
    if ret is False:
        break
    roi=frame[80:210,230:450]
    row,col,chanel=roi.shape # once satir sonra sutun sonrada kanal  degerini verir.
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    a,thresh=cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)# thresh degerini 50, max i 255, ve binary inverse u kullandik(siyahlar beyaz, beyazlar siyah olur)
    
    contours,b=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours=sorted(contours,key= lambda x:cv2.contourArea(x),reverse=True )# konturlari alani en buyukten kucuge dogru siraladik, en buyuk olan goz bebegine ait.
    
    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)# konturun basladigi noktalar x ve y, w: saga dogru genisligi(width),h: uzunlugu(height)

        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),row),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(col,y+int(h/2)),(0,255,0),2)
        break

    
    frame[80:210,230:450]=roi # roi deki goruntuyu frame e kopyaladik

    cv2.imshow("roi",roi)
    cv2.imshow("thresh",thresh)
    cv2.imshow("frame",frame)
    if cv2.waitKey(80)& 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
