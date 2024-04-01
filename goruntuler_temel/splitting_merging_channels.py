import cv2
import numpy as np
import matplotlib.pyplot as plt

path="test_images/opencv_logo.png"
img=cv2.imread(path)

cv2.imshow("open",img)
(b,g,r)=cv2.split(img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
merge=cv2.merge([b,g,r])
cv2.imshow("merge",merge)

black=np.zeros(img.shape[:2],dtype="uint8") # img nin boyutu kadar sifirlardan (siyahlardan) olusan bir matris olusturduk
cv2.imshow("black",black)
cv2.imshow("blue",cv2.merge([b,black,black]))
cv2.imshow("green",cv2.merge([black,g,black]))
cv2.imshow("red",cv2.merge([black,black,r]))
print("shape: {}".format(img.shape))
print("dtype:{}".format(img.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
