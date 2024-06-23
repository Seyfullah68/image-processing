import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("C:\\Users\\seyfu\\Downloads\\coins.jpg")

print(img);print("size:",img.size);print("type:",type(img));print("ndim:",img.ndim);print("shape:",img.shape)

print("red channel:",img[50,50,0])#rgb, r:0,g:1:b:2
print("green channel:",img[50,50,1])
print("blue channel:",img[50,50,2])
print("rgb channel:",img[50,50,:])
plt.imshow(img)
plt.show()