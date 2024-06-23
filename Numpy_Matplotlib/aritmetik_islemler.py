import matplotlib.pyplot as plt
import numpy as np

img=plt.imread("C:\\Users\\seyfu\\Downloads\\map.jpg")

plt.subplot(4,2,1)
plt.title("orjinal")
plt.imshow(img)

plt.subplot(4,2,2)
plt.title("img+img")
plt.imshow(img+img)

plt.subplot(4,2,3)
plt.title("img-img")
plt.imshow(img-img)

plt.subplot(4,2,4)
plt.title("flip-0")
plt.imshow(np.flip(img,0))

plt.subplot(4,2,5)
plt.title("flip-1")
plt.imshow(np.flip(img,1))

plt.subplot(4,2,6)
plt.title("flip-2")
plt.imshow(np.flip(img,2))

plt.subplot(4,2,7)
plt.title("flip-lr")
plt.imshow(np.fliplr(img))#lr: left to right

plt.subplot(4,2,8)
plt.title("flip-ud")
plt.imshow(np.flipud(img))#ud: upside down 



plt.show()
