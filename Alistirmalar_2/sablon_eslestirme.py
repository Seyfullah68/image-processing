import cv2
import numpy as np

img1=cv2.imread("starwars.jpg")
img2=cv2.imread("starwars2.jpg")

img1_gri=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2_gri=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
w,h=img2_gri.shape[::-1]# -1 koyarak x ve y degerlerinin yerlerini degistirdik
result=cv2.matchTemplate(img1_gri,img2_gri,cv2.TM_CCOEFF_NORMED)# iki sablonu karsilastirdik

locations=np.where(result>0.9)# eslesmenin 0.7 den buyuk oldugu(beyaz renk e yakin olan kisimlar) yerlerin lokasyonlarini aldik
print(locations)
for points in zip(*locations[::-1]): # lokasyonda x ve y lerin yerlerini degistirip, koordinatlri belirledik,zip ile x ve y leri eslestirdik. 
    print(points)
    cv2.rectangle(img1,points,(points[0]+w,points[1]+h),(0,0,255),3)


cv2.imshow("img1",img1)
cv2.imshow("img2",img2_gri)
cv2.imshow("results",result)#eslesmede ikinci sablonun sol ust kosesi beyaz renk alir

cv2.waitKey(0)
cv2.destroyAllWindows()