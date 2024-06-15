import cv2
import numpy as np
from collections import deque

vid=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)

lower_blue=np.array([100,60,60])
upper_blue=np.array([140,255,255])

blue_points=[deque(maxlen=512)]#max 512 sayi tutabilen bos bir matris tanimladik
green_points=[deque(maxlen=512)]
red_points=[deque(maxlen=512)]
yellow_points=[deque(maxlen=512)]

blue_index=0
green_index=0
red_index=0
yellow_index=0

colors=[(255,0,0),(0,255,0),(0,0,255),(0,255,255)]#mavi yesil kirmizi ve sari renkleri
colors_index=0

paint_window=np.zeros((471,636,3))+255# 3 kanalli cizim yapacagimiz beyaz ekrani olusturduk
paint_window=cv2.rectangle(paint_window,(40,1),(140,65),(0,0,0),2) # ekrandaki dikdortgenleri olusturduk
paint_window=cv2.rectangle(paint_window,(160,1),(255,65),colors[0],-1)
paint_window=cv2.rectangle(paint_window,(275,1),(370,65),colors[1],-1)
paint_window=cv2.rectangle(paint_window,(390,1),(485,65),colors[2],-1)
paint_window=cv2.rectangle(paint_window,(505,1),(600,65),colors[3],-1)

font=cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(paint_window,"Clear All",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA) # dikdortgenlerin isimlerini yazdik
cv2.putText(paint_window,"Blue",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"Green",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"Red",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"Yellow",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow("paint")

while 1:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#goruntuyu hsv formatina cevirdik

    
    frame=cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2) # ekrandaki dikdortgenleri olusturduk
    frame=cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame=cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame=cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame=cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)

    font=cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,"Clear All",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA) # dikdortgenlerin isimlerini yazdik
    cv2.putText(frame,"Blue",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"Green",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"Red",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"Yellow",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

    if ret is False: # eger video bittiyse yada okuma yapilamadiysa cikis ilemi yapilir
        break

    mask=cv2.inRange(hsv,lower_blue,upper_blue)#mavi rengi icin maskeleme islemini yaptik

    mask=cv2.erode(mask,kernel,iterations=2) #goruntudeki karincalanlamalari azattik
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.dilate(mask,kernel,iterations=1)#cizgileri daha kalinlastirdik

    contours,a=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# konturlari bulduk

    center=None # cismin merkezi icin belirledik

    if len(contours)>0:
        max_contour=sorted(contours,key=cv2.contourArea,reverse=True)[0]#konturlarin alanlarini buyukten kucuge siraladik, en buyugu sectik

        ((x,y),r)=cv2.minEnclosingCircle(max_contour)# max konturu cevreleyen cemberin merkez ve yaricapini bulduk

        cv2.circle(frame,(int(x),int(y)),int(r),(220,45,78),3)#frame e cemberi cizdik

        M=cv2.moments(max_contour)# kontur un merkez noktasini bulduk
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))#cismin merkezini bulduk

        if center[1]<=65:#eger cismin merkezinin y si 65 ten kucukse
            if 40<= center[0]<=140:#clear all butonu
                blue_points=[deque(maxlen=512)]#max 512 sayi tutabilen bos bir matris tanimladik
                green_points=[deque(maxlen=512)]
                red_points=[deque(maxlen=512)]
                yellow_points=[deque(maxlen=512)]

                blue_index=0
                green_index=0
                red_index=0
                yellow_index=0

                paint_window[67:,:,:]=255 # butonlardan asagisini komple temizledik
            
            elif 160<= center[0] <=255:# mavi kutuda ise
                colors_index=0
            
            elif 275<= center[0] <= 370:# yesil kutuda ise
                colors_index=1
            
            elif 390<= center[0] <= 485:#kirmizi kutuda ise
                colors_index=2
            
            elif 505<= center[0] <= 600:#sari kutuda ise
                colors_index=3

        else:
            if colors_index==0:
                blue_points[blue_index].appendleft(center)#merkezin degerlerini listenin soluna ekledik

            elif colors_index==1:
                green_points[green_index].appendleft(center)
            
            elif colors_index==2:
                red_points[red_index].appendleft(center)
            
            elif colors_index==3:
                yellow_points[yellow_index].appendleft(center)
            
    else:
        blue_points.append(deque(maxlen=512))
        blue_index+=1

        green_points.append(deque(maxlen=512))
        green_index+=1

        red_points.append(deque(maxlen=512))
        red_index+=1

        yellow_points.append(deque(maxlen=512))
        yellow_index+=1

    points=[blue_points,green_points,red_points,yellow_points]

    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(len(points[i][j])):
                if points[i][j][k-1] is None or points[i][j][k] is None:# eger bu degerler bos degilse devam et demek
                    continue
                cv2.line(frame,points[i][j][k-1],points[i][j][k],colors[i],2)

                cv2.line(paint_window,points[i][j][k-1],points[i][j][k],colors[i],2)


    cv2.imshow("frame",frame)
    cv2.imshow("paint",paint_window)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
