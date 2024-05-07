import cv2
import numpy as np

img=cv2.imread("star.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#resmi gri tonuna cevirdik
a,thresh=cv2.threshold(gri,127,255,0)# threasholdlari bulduk

contours,b=cv2.findContours(thresh,2,1) # contourlari bulduk

cnt=contours[0]

hull=cv2.convexHull(cnt,returnPoints=False) # convexhullari bulduk

defects=cv2.convexityDefects(cnt,hull) # defectsleri bulduk

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0] #s: start point,e: end point, f: farest point, d: distence 

    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])

    cv2.line(img,start,end,(0,255,0),3)
    cv2.circle(img,far,5,(0,0,255),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
