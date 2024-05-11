import cv2
import numpy as np

img1= cv2.imread("coins.jpg")

gri1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

blur1=cv2.medianBlur(gri1,5) # resimdeki gurultuyu azattik


circle1=cv2.HoughCircles(blur1,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=80)# circle lari bulduk, param1: gradient parametresi,param2:threshold, img.shape/64 : daireler arasi mesafe
print(circle1)
if circle1 is not None:
    circle1=np.uint16(np.around(circle1))# degerleri yuvarlayip uint16 tipine cevirdik
    for i in circle1[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],(0,0,255),3) # daireleri orjinal resime cizdik

cv2.imshow("img1",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
