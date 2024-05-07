import cv2


img=cv2.imread("ucgen.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

a,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

m=cv2.moments(thresh)  # bu fonk. ciktisi matris sayesinde gorselin geometrik merkezini buluruz

print(m)# burada degerleri goruyoruz
x=int(m["m10"]/m["m00"]) # geo. merkezin x degerini bulduk
y=int(m["m01"]/m["m00"]) # geo. merkezin y degerini bulduk

cv2.circle(img,(x,y),7,(0,0,0),-1) # geometrik merkeze daire ekledik

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()