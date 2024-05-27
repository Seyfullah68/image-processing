import cv2
import numpy as np

img1=cv2.imread("aircraft.jpg")
img2=cv2.imread("aircraft1.jpg")

img1=cv2.resize(img1,(640,480))
img2=cv2.resize(img2,(640,480))


if img1.shape==img2.shape:

    print("same size")
else:
    print("different size")

diff=cv2.subtract(img1,img2)# iki resimi birbirinden cikarir.Farkli olan kisimlar beyaz, ayni olanlar siyah olur.

b,g,r=cv2.split(diff)# katmanlara ayirma islemi

if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:# b,g,r da beyazlari saydik.
    print("same figures")
else:
    print("different figures")




cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("diff",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()