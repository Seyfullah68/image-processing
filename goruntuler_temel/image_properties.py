import cv2
import numpy as np
import matplotlib.pyplot as plt

path= "test_images/opencv_logo.png"
img=cv2.imread(path)
img2=cv2.imread(path,0)
cv2.imshow("test",img)
cv2.imshow("grayscale",img2)
print(img.shape) # y degeri, x degeri ve number of chanel sayisini sirasi ile gosterir.
#kanal katman sayisidir, 3 ise ayni resimden 3 katman var demektir
# channel =3 : renki 
# channel =1 : grayscale (siyah beyaz)

print("yukseklik: {}".format(img.shape[0]))
print("genislik:{}".format(img.shape[1]))
print("channel:{}".format(img.shape[2]))

print("image size :{}".format(img.size))  # yukseklik*genislik*kanal sayisi
print("image data type : {}".format(img.dtype)) # uint8 : unsigned integer 8 tipinde
cv2.waitKey(0)
cv2.destroyAllWindows()