import cv2
import numpy as np

img1=cv2.imread("contour.png")
img2=cv2.imread("text.png")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

gray1=np.float32(gray1) # asagidaki fonk. u kullanmak icin float degerlerine cevirdik
gray2=np.float32(gray2)
corners=cv2.goodFeaturesToTrack(gray1,50,0.01,10) # koseleri belirledik, 0.01 i sabit bir deger gibi dusunebiliriz.
corners2=cv2.goodFeaturesToTrack(gray2,100,0.01,10)
corners=np.int0(corners) # resmi goruntulemek icin tekrardan int a cevirdik. 
corners2=np.int0(corners2)

for corner in corners:
    x,y=corner.ravel() # bu fonk. ile noktanin x, y degerlerini aldik.
    cv2.circle(img1,(x,y),3,(0,0,255),-1) # koselere daire cizdik

cv2.imshow("contour",img1)
for corner2 in corners2:
    x,y=corner2.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)

cv2.imshow("text",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
