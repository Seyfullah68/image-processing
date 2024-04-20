import cv2
import numpy as np
from matplotlib import pyplot as plt

"""img=np.zeros((500,500),dtype=np.uint8)+50
cv2.rectangle(img,(50,50),(250,300),(255,255,255),-1)
cv2.imshow("img",img)  """ 
img2=cv2.imread("klon.jpg")
cv2.imshow("klon",img2)
"""plt.hist(img2.ravel(),256,[0,256])# 0-256 arasi 256 deger gosterir. Y ekseni 500*500, x ekseni ise 0-256 arasi.
plt.show()"""
b,g,r=cv2.split(img2)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
