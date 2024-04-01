import cv2
import numpy as np
import matplotlib.pyplot as plt

path="test_images/orman.jpg"

img=cv2.imread(path)
#print(img)
kose=img[0:100,0:100]
kose2=img[0:100,0:250] # [y,x] : kordinatlar
cv2.imshow("orman",img)
cv2.imshow("kose",kose)
cv2.imshow("kose2",kose2)
img2=img
img2[0:100,0:250]=(255,0,0)
cv2.imshow("mavi",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
