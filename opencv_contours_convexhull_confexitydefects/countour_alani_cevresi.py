import cv2

img=cv2.imread("ucgen.png")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

a,thresh=cv2.threshold(gri,127,255,cv2.THRESH_BINARY)# goruntuyu binary(siyah ve beyaza cevirdik)

contours,b=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# siyah beyaz goruntudeki kenarlari belirledik
cvt=contours[0]

area=cv2.contourArea(cvt) # kontor ile bu fonk. kullanarak alani bulduk
print(area)

M=cv2.moments(cvt) # momentlari bulduk
print(M["m00"]) # momentlarin ilk degeri alani verir

cevre=cv2.arcLength(cvt,True)# cevreyi bulduk, sekil kapali oldugu icin true girdik
print(cevre)

cv2.imshow("orj",img)
cv2.imshow("gri",gri)
cv2.imshow("threash",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()