import cv2

cv2.namedWindow("klonum",cv2.WINDOW_NORMAL)
img=cv2.imread("klon.jpg",0)
img=cv2.resize(img,(600,400))
cv2.imshow("klonum",img)
cv2.waitKey(0)
cv2.destroyAllWindows()