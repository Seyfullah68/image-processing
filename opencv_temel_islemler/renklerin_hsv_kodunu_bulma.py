import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow("track_bar",cv2.INTER_AREA)
cv2.resizeWindow("track_bar",400,400)

def bos(x):  # create trackbar fonkiyonu fonksiyon girmemizi istedigi icin zorunlu yaptik.
    pass
#tracbarlari olusturduk
cv2.createTrackbar("lower-h","track_bar",0,180,bos)
cv2.createTrackbar("lower-s","track_bar",0,255,bos)
cv2.createTrackbar("lower-v","track_bar",0,255,bos)

cv2.createTrackbar("higher-h","track_bar",0,180,bos)
cv2.createTrackbar("higher-s","track_bar",0,255,bos)
cv2.createTrackbar("higher-v","track_bar",0,255,bos)

cv2.setTrackbarPos("higher-h","track_bar",180)
cv2.setTrackbarPos("higher-s","track_bar",255)
cv2.setTrackbarPos("higher-v","track_bar",255)



while True:
    rec,frame=cap.read()# videonun true false ve goruntusunu aldik
    frame=cv2.flip(frame,1) # goruntuyu y ekseninde ters cevirdik
    if rec==False:
        break

    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # goruntuyu hsv renk uzayina cevirdik
    # trackbar degerlerini aldik
    low_h=cv2.getTrackbarPos("lower-h","track_bar")
    low_s=cv2.getTrackbarPos("lower-s","track_bar")
    low_v=cv2.getTrackbarPos("lower-v","track_bar")

    high_h=cv2.getTrackbarPos("higher-h","track_bar")
    high_s=cv2.getTrackbarPos("higher-s","track_bar")
    high_v=cv2.getTrackbarPos("higher-v","track_bar")

    low=np.array([low_h, low_s, low_v])
    high=np.array([high_h, high_s ,high_v])

    mask=cv2.inRange(frame_hsv,low,high) # inrange fonk. ile bu trackbar degerlerini ve goruntuyu girdik,filtremeyi bu fonk. ile yaptik.
    cv2.imshow("canli",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

   

cap.release()
cv2.destroyAllWindows()
