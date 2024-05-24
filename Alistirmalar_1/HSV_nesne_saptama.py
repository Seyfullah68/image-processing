import cv2
import numpy as np

vid=cv2.VideoCapture("hsv.mp4")
def nothing(x): # trackbar olustururken fonk girmemiz gerekiyor. O yuzden olusturduk
    pass
cv2.namedWindow("trackbar")# trackbar larin penceresi

cv2.createTrackbar("LH","trackbar",0,180,nothing) # trackbar lari olusturduk
cv2.createTrackbar("LS","trackbar",0,255,nothing)
cv2.createTrackbar("LV","trackbar",0,255,nothing)
cv2.createTrackbar("UH","trackbar",0,180,nothing)
cv2.createTrackbar("US","trackbar",0,255,nothing)
cv2.createTrackbar("UV","trackbar",0,255,nothing)

while True:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,480)) # frame i yeniden sekillendirdik
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # hsv formatina cevirdik

    lh=cv2.getTrackbarPos("LH","trackbar") # trackbarlarin degerlerini aldik
    ls=cv2.getTrackbarPos("LS","trackbar")
    lv=cv2.getTrackbarPos("LV","trackbar")
    uh=cv2.getTrackbarPos("UH","trackbar")
    us=cv2.getTrackbarPos("US","trackbar")
    uv=cv2.getTrackbarPos("UV","trackbar")

    lower=np.array([lh,ls,lv])
    upper=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower,upper) # mask uyguladik

    bitwise=cv2.bitwise_and(frame,frame,mask=mask) # bitwise ile mask sonrasindaki goruntu rengi orjinali ile ayni olur

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break


vid.release()
cv2.destroyAllWindows()