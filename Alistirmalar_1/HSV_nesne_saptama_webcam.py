import cv2
import numpy as np

vid=cv2.VideoCapture(0)
def bos(x):
    pass
cv2.namedWindow("trackbar")

cv2.createTrackbar("lh","trackbar",0,180,bos)
cv2.createTrackbar("ls","trackbar",0,255,bos)
cv2.createTrackbar("lv","trackbar",0,255,bos)
cv2.createTrackbar("uh","trackbar",0,180,bos)
cv2.createTrackbar("us","trackbar",0,255,bos)
cv2.createTrackbar("uv","trackbar",0,255,bos)
while True:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame=cv2.resize(frame,(640,480))
    Lh=cv2.getTrackbarPos("lh","trackbar")
    Ls=cv2.getTrackbarPos("ls","trackbar")
    Lv=cv2.getTrackbarPos("lv","trackbar")
    Uh=cv2.getTrackbarPos("uh","trackbar")
    Us=cv2.getTrackbarPos("us","trackbar")
    Uv=cv2.getTrackbarPos("uv","trackbar")

    lower=np.array([Lh,Ls,Lv])
    upper=np.array([Uh,Us,Uv])

    mask=cv2.inRange(hsv,lower,upper)
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
