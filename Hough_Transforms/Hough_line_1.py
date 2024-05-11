import cv2
import numpy as np

img=cv2.imread("h_line.png")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#resimi gri tonuna cevirdik

edges=cv2.Canny(gri,75,150) # resimde koseleri bulduk. Threshold degerlerini 75 ve 150 girdik. 

lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200) # cizgileri cizdik ve max. line gap e gore bosluklar tamamlandi

print(lines)

for line in lines:
    x1,y1,x2,y2=line[0] # noktalar baslangic ve bitis koordinatlari
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("img",img)
cv2.imshow("gri",gri)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
