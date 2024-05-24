import cv2 
import numpy as np

vid=cv2.VideoCapture("car.mp4")
"""ilk frame i cekiyoruz, gri tona ceviriyoruz, blur uygulayip gurultuyu azaltiyoruz
sonrasinda ilk frame ile diger frameleri karsilastirarak hareket eden arabalari tespit ediyoruz"""
a,first_frame = vid.read()
first_frame=cv2.resize(first_frame,(640,480))
first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray=cv2.GaussianBlur(first_gray,(5,5),0)


while True:
    a,frame=vid.read()
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(5,5),0)# blur uygulayip frame deki gurultuyu azalttik    

    diff=cv2.absdiff(first_gray,gray) # ilk frame ile anlik frame in farkini aldik

    a,diff=cv2.threshold(diff,50,255,cv2.THRESH_BINARY)# threshold uygulayarak siyah ve beyazlari daha netledik

    cv2.imshow("first",first_frame)
    cv2.imshow("frame",frame)
    cv2.imshow("diff",diff)

    if cv2.waitKey(20)&0xFF==ord("q"):
        break
vid.release()
cv2.destroyAllWindows()
