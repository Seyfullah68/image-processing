import cv2
import numpy as np
import matplotlib as plt

img=cv2.imread("kus.png") # resmi okuduk

def bos(x): # trackbar lar icin gerekli
    pass
cv2.namedWindow("trackbar") # trackbarlarin cercevesini olusturduk

cv2.createTrackbar("h_lower","trackbar",0,180,bos) # trackbarlari olusturduk
cv2.createTrackbar("s_lower","trackbar",0,255,bos)
cv2.createTrackbar("v_lower","trackbar",0,255,bos)
cv2.createTrackbar("h_upper","trackbar",0,180,bos)
cv2.createTrackbar("s_upper","trackbar",0,255,bos)
cv2.createTrackbar("v_upper","trackbar",0,255,bos)
while 1:
    
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #resmi hsv formatina cevirdik
    
    lower_h=cv2.getTrackbarPos("h_lower","trackbar") #trackbarlarin degerlerini aldik
    lower_s=cv2.getTrackbarPos("s_lower","trackbar")
    lower_v=cv2.getTrackbarPos("v_lower","trackbar")
    upper_h=cv2.getTrackbarPos("h_upper","trackbar")
    upper_s=cv2.getTrackbarPos("s_upper","trackbar")
    upper_v=cv2.getTrackbarPos("v_upper","trackbar")

    lower=np.array([lower_h,lower_s,lower_v]) #maskeleme icin degerleri dizide tuttuk
    upper=np.array([upper_h,upper_s,upper_v])

    mask=cv2.inRange(img_hsv,lower,upper) # maskeleme islemini yaptik

    result=cv2.bitwise_and(img,img,mask=mask) # maskeyi orjinal gorsele uyguladik
    
    cv2.imshow("mask",mask)
    cv2.imshow("results",result)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()