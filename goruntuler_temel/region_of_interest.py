import cv2
import numpy as np
import matplotlib.pyplot as plt

path="test_images/basketball.jpg"
img=cv2.imread(path)
roi=img[100:200,0:50]
img2=img
img2[300:400,300:350]=roi
cv2.imshow("resim",img)
cv2.imshow("kafa",roi)
cv2.imshow("yapistir",img2)
print("boyutlar:{}".format(img.shape))

cv2.waitKey(0)
cv2.destroyAllWindows()