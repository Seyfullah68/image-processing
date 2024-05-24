import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX # yazi fontlarini belirledik
font1=cv2.FONT_HERSHEY_COMPLEX
img=cv2.imread("polygons.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # resmi gri ye cevirdik

a,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # threshold ile siyah beyaz yaptik

contours,a=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # resmin koselerini belirledik

for cnt in contours:
    # yaklasim islemlerini yapiyoruz:
    epsilon=0.01*cv2.arcLength(cnt,True)# contourlarin boyu ve kapali sekil oldugunu girdik, ciktiyi 0.01 ile carptik
    approx=cv2.approxPolyDP(cnt,epsilon,True)# yaklasim islemini yaptik
    cv2.drawContours(img,[approx],0,(0),5) # contourlari cizdik

    x=approx.ravel()[0] # yazi yazacagimiz koordinatari belirledik
    y=approx.ravel()[1]

    # yazi yazma islemi:
    if len(approx)==3:
        cv2.putText(img,"ucgen",(x,y),font,1,(0,0,255),3)
    elif len(approx)==4:
        cv2.putText(img,"dortgen",(x,y),font,1,(0,0,255),3)
    elif len(approx)==5:
        cv2.putText(img,"besgen",(x,y),font1,1,(0,0,255),3)
    elif len(approx)==6:
        cv2.putText(img,"altigen",(x,y),font1,1,(0,0,255),3)
    else:
        cv2.putText(img,"elips",(x,y),font1,1,(0,0,255),3)
    
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()





