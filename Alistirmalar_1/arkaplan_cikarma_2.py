import cv2
import numpy as np

vid=cv2.VideoCapture("car.mp4")
subsractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)# bu fonk ile arka plani cikarma islemi yapilir

while True:

    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,480))

    mask=subsractor.apply(frame)

    cv2.imshow("orj",frame)
    cv2.imshow("substracted",mask)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()