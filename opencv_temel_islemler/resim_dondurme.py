import cv2
import numpy as np

img=cv2.imread("klon.jpg",0)
row,col=img.shape

M=cv2.getRotationMatrix2D((col/2,row/2),180,1)# dondurme icin matrix degerlerini aldik

rd=cv2.warpAffine(img,M,(col,row)) # dondurme islemini yaptik
cv2.imshow("orj",img)
cv2.imshow("rotated",rd)

cv2.waitKey(0)
cv2.destroyAllWindows()
