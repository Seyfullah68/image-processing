import cv2
import numpy as np

video=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_COMPLEX
def nothing(x):
    pass

cv2.namedWindow("trackbar")

cv2.createTrackbar("lower_hue","trackbar",0,180,nothing)
cv2.createTrackbar("lower_saturation","trackbar",0,255,nothing)
cv2.createTrackbar("lower_value","trackbar",0,255,nothing)
cv2.createTrackbar("upper_hue","trackbar",0,180,nothing)
cv2.createTrackbar("upper_saturation","trackbar",0,255,nothing)
cv2.createTrackbar("upper_value","trackbar",0,255,nothing)

while True:
    ret,frame=video.read()

    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_h=cv2.getTrackbarPos("lower_hue","trackbar")
    lower_s=cv2.getTrackbarPos("lower_saturation","trackbar")
    lower_v=cv2.getTrackbarPos("lower_value","trackbar")
    upper_h=cv2.getTrackbarPos("upper_hue","trackbar")
    upper_s=cv2.getTrackbarPos("upper_saturation","trackbar")
    upper_v=cv2.getTrackbarPos("upper_value","trackbar")

    lower=np.array([lower_h,lower_s,lower_v])
    upper=np.array([upper_h,upper_s,upper_v])

    mask=cv2.inRange(hsv,lower,upper)
    kernel=np.ones((5,5),np.uint8) # 5x5 lik birlerden olusan bir matris tanimladik
    mask=cv2.erode(mask,kernel) # mask i ereyona ugrattik. Yani beyazlar icindeki siyah noktalari sildik. 

    contours,a=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area=cv2.contourArea(cnt) # contourlarin alanlarini bulduk
        epsilon=0.02*cv2.arcLength(cnt,True) # matematiksel epsilon degerini bulduk
        aprox=cv2.approxPolyDP(cnt,epsilon,True) # yaklasimlari yaptik 

        x=aprox.ravel()[0] # contourlarin baslangic x noktasini bulduk
        y=aprox.ravel()[1] # contourlarin baslangic y noktasini bulduk

        if area>400: # eger contour alani 400 den buyukse, o bolgeye islem yaptik
            cv2.drawContours(frame,[aprox],0,(0,0,255),5)
            if len(aprox)==3:
                cv2.putText(frame,"ucgen",(x,y),font,1,(0,0,0),3)
            elif len(aprox)==4:
                cv2.putText(frame,"dortgen",(x,y),font,1,(0,0,0),2)
            else :
                cv2.putText(frame,"daire",(x,y),font,1,(0,0,0),3)

            



    cv2.imshow("orj",frame)
    cv2.imshow("filtered",mask)

    if cv2.waitKey(5) & 0xFF==("q"):
        break

video.release()
cv2.destroyAllWindows()
