import cv2
import numpy as np

def nothing(x):
    pass

img=np.zeros((512,512,3),dtype=np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("R","image",0,255,nothing) # trackbar lari olusturduk, cv2 fonksiyon istedigi icin bos bir fonk. girdik
cv2.createTrackbar("G","image",0,255,nothing) # trackbarlari image penceresine yerlestirdik. 
cv2.createTrackbar("B","image",0,255,nothing)
switch="0: off, 1:onn"
cv2.createTrackbar(switch,"image",0,1,nothing)

while True:
    cv2.imshow("image",img)
    r=cv2.getTrackbarPos("R","image") # image penceresindeki trackbar daki girilen degerleri degiskenlere esitledik.
    g=cv2.getTrackbarPos("G","image")
    b=cv2.getTrackbarPos("B","image")
    s=cv2.getTrackbarPos(switch,"image")
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    if s==0:
        img[:]=[0,0,0] # eger switch 0 ise img nin butun degerleri sifirlanir, bu da siyah renk verir
    if s==1:
        img[:]=[b,g,r] # eger switch 1 ise img nin degerliri trackbar daki degerlere esitlenir 

cv2.destroyAllWindows()

