import cv2
import numpy as np

img=cv2.imread("klon.jpg",0)# gri tonunda okuma yaptik
row,col=img.shape
cv2.imshow("img",img)
print(row)
print(col)

M=np.float32([[1,0,10],[0,1,150]]) # resmi 10,150 kadar kaydiracak matrix degerleri aldik. 
rdd=cv2.warpAffine(img,M,(row,col)) # resmin kaydirma islemini yaptik
cv2.imshow("kaydirilmis",rdd)
cv2.waitKey(0)
cv2.destroyAllWindows()