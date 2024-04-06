import cv2
import numpy as np

img=np.zeros((10,10,3),dtype=np.uint8)
#img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)# interpolaston: resmin merkezini korumak icin kullaniriz
#cv2.imshow("img",img)
img[0,0]=(255,255,255)
img[0,1]=(255,255,200)
img[0,2]=(255,255,100)
img[0,3]=(255,255,5)

img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)
cv2.imshow("img2",img)
#black&white
resim=np.zeros((10,10),dtype=np.uint8)
resim[0,0]=255
resim[0,1]=200
resim[0,2]=100
resim[0,3]=5
resim=cv2.resize(resim,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow("b&w",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()