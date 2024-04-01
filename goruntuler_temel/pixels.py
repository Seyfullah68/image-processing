import cv2
import numpy as np

url ="test_images/opencv_logo.png"
img= cv2.imread(url)

#print(img)
#print(img[0,0])

(b,g,r)=img[50,30] # 50(x) ye 30(y) kordinatindaki pixel degerleri

print("(0,0) red:{}, green:{}, blue:{}".format (r,g,b))


"""
BGR/RGB RENKLENDIRME SISTEINDE:

BLUE: 0-255 ARASI
GREEN: 0-255 ARASI
RED: 0-255 ARASI

0: BLACK
255: WHITE DEMEKTIR. 
ORNEK: BLUE 255, RED 0, GREEN 0,  SONUC= BLUE

"""
# pixellere erisme - 1

print("before:",img[100,100])
img[100,100]=[100,100,100] 
print("after:",img[100,100])

blue=img[50,30,0] # listenin 0. indexi blue
green=img[50,30,1] # listenin 1. indexi green
red=img[50,30,2] # listenin 2. indexi red

# pixellere erisme -2

print("red value:(before)",img.item(10,10,2))
img.itemset((10,10,2),100)
print("red value:(after)",img.item(10,10,2))
