import cv2

img=cv2.imread("aircraft.jpg")

blur=cv2.medianBlur(img,5)

laplacian=cv2.Laplacian(blur,cv2.CV_64F).var() # resimde blur arttikca bu deger kuculur. bu ornekt

print(laplacian)
if laplacian < 500:
    print("blurlu")


cv2.imshow("img",img)
cv2.imshow("blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
