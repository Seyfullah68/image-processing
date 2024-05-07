import cv2
import numpy as np

img=cv2.imread("map.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gri,(3,3)) # goruntuyu biraz daha blurladik(bulaniklasti).
a,thresh=cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

contours,hiyerarsi=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# konturlari bulduk
hull=[]

for i in range(len(contours)): # konturlarin uzunlugu kadar bir dongu
    hull.append(cv2.convexHull(contours[i])) 
#convex hull larin degerlerini hull dizisine ekledik

siyah=np.zeros((thresh.shape[0],thresh.shape[1],3),dtype=np.uint8) # siyah bir ekran olusturduk thresh boyutunda ve 3 boyutlu


for i in range(len(contours)):
    cv2.drawContours(siyah,contours,i,(255,0,0),3,8)# konturlari siyah ekrana cizdik
    cv2.drawContours(siyah,hull,i,(0,255,0),1,8)# hulllari siyah ekrana cizdik




cv2.imshow("orj",img)
cv2.imshow("gri",gri)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
cv2.imshow("concexhull_kontors",siyah)
cv2.waitKey(0)
cv2.destroyAllWindows()
