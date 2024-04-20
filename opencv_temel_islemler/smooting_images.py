import cv2
import numpy as np

img_filter=cv2.imread("filter.png")
img_median=cv2.imread("median.png")
img_bilateral=cv2.imread("bilateral.png")
blur=cv2.blur(img_filter,(11,11)) # goruntuyu blur(bulaniklik) lastirir. int degerler pozitif teksayi olmak zorunda

cv2.imshow("orginal",img_filter)
cv2.imshow("blur",blur)

blur_m=cv2.medianBlur(img_median,7) # resimdeki gurultuyu azaltir, girilen int deger pozitif teksayi olmali

cv2.imshow("median_orj",img_median)
cv2.imshow("median_blur",blur_m)

bilateral=cv2.bilateralFilter(img_bilateral,9,95,95) # orjinal resimdeki puturleri yok eder
cv2.imshow("img_bil_org",img_bilateral)
cv2.imshow("bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
