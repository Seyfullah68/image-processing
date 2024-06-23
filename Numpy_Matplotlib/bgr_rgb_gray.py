import cv2
import matplotlib.pyplot as plt

path="C:\\Users\\seyfu\\Downloads\\smile.jpg"

img=cv2.imread(path)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img)#resim rgb olarak gosteriliyor
plt.imshow(img_rgb)#resim normal gosterilir
plt.imshow(gray,cmap="gray",interpolation="BICUBIC")#cmap:color map
plt.show()