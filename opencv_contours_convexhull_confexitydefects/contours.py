import cv2

img=cv2.imread("contour1.png")
cv2.imshow("orj",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

a,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#127 ve 255 boyut degerleri, binary ise 0 veya 1 donmesi icin

contours,b=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# bu iki fonksiyon kordinatlari daha dogru bulmayi saglar

print(contours)

#Contours lari cizdirme islemi

cv2.drawContours(img,contours,-1,(0,0,255),3) # countour index i -1 girdik (dis pencereyi de cizdi)

cv2.imshow("contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
