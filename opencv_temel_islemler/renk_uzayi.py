import cv2
import numpy as np

img=cv2.imread("klon.jpg")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img4=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gri resimlerde isleme her zaman daha kolaydir, cunku katman sayisi azdir
cv2.imshow("klon BGR",img)
cv2.imshow("klon RGB",img2)
cv2.imshow("klon HSV",img3)
cv2.imshow("klon GRAY",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
