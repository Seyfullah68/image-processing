import cv2
import numpy as np
import math

vid=cv2.VideoCapture(0)
while True:
    try:
        ret,frame=vid.read()

        frame=cv2.flip(frame,1)
        kernel=np.ones((3,3),dtype=np.uint8)
        roi=frame[100:300,100:300]
        cv2.rectangle(frame,(100,100),(300,300),(0,0,255),2)
        hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        lower_skin=np.array([0,15,50],dtype=np.uint8)#degerleri internetten bulduk
        upper_skin=np.array([20,255,255],dtype=np.uint8)

        mask=cv2.inRange(hsv,lower_skin,upper_skin)
        mask=cv2.dilate(mask,kernel,iterations=4)#maskda belirlenen yeri 4 katman beyazlatma islemi(cunku kernel 1 lerden olusuyor)
        mask=cv2.GaussianBlur(mask,(5,5),100)#resimdeki gurultuyu azalttik (blurladik)

        contours,a=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cnt=max(contours,key=lambda x : cv2.contourArea(x))#contourlarin alanlarina gore bakip, en buyugu bulduk

        epsilon=0.0005*cv2.arcLength(cnt,True)#kapali sekil oldugu icin true
        approx=cv2.approxPolyDP(cnt,epsilon,True)#contourslara yaklasim yaptik(iyilestirme), kapali sekil oldugu icin true. 

        hull=cv2.convexHull(cnt)

        area_hull=cv2.contourArea(hull)
        area_cnt=cv2.contourArea(cnt)
        area_ratio=((area_hull-area_cnt)/area_cnt)*100# elin olmadigi alanin yuzdesini bulduk

        hull=cv2.convexHull(approx,returnPoints=False)#false oldugu ,c,n kontourlarin indisleri cikti olur
        defects=cv2.convexityDefects(approx,hull)#hatalari bulduk

        hata=0

        for i in range(defects.shape[0]):
            s,e,f,d=defects[i,0]#convex hull un(dis ortu) koordinatlarini bulduk
            start=tuple(approx[s][0])
            end=tuple(approx[e][0])
            far=tuple(approx[f][0])
             
            a=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2) # olusan ucgenin kenar uzunluklarini hesapladik
            b=math.sqrt((far[0]-start[0])**2+(far[1]-start[1])**2)
            c=math.sqrt((end[0]-far[0])**2+(end[1]-far[1])**2)

            s=(a+b+c)/2

            area=math.sqrt(s*(s-a)*(s-b)*(s-c))#kenar uzunluklarini bildigimiz ucgenin alani
            d=(2*area)/a#contours ve convex hull arasindaki hatayi bulmak icin hesapladik

            angle=math.acos((b**2+c**2-a**2)/(2*b*c))*57 # aciyi bulduk

            if angle<=90 and d>30:
                hata+=1
                cv2.circle(roi,far,3,[255,0,0],-1)#parmak aralarina ici dolu ucgen cizdik

            cv2.line(roi,start,end,[255,0,0],2)# parmaklarin cizgilerini cizdik
        
        hata+=1

        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

        if hata==1:
            if area_cnt<2000: # daha once denenmis bir deger
                cv2.putText(frame,"elini kutuya getir",(0,50),font,1,(0,0,255),2,lineType=cv2.LINE_AA)
            else:
                if area_ratio<12: # denenmis deger
                    cv2.putText(frame,"0",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
                elif area_ratio<17.5:
                    cv2.putText(frame,"iyi sanslar",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
                else:
                    cv2.putText(frame,"1",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
        
        elif hata==2:
            cv2.putText(frame,"2",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)

        elif hata==3:
            if area_ratio<27:
                cv2.putText(frame,"3",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
            else:
                cv2.putText(frame,"ok",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
                
        elif hata==4:
            cv2.putText(frame,"4",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
        
        elif hata==5:
            cv2.putText(frame,"5",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)
        
        else :
            cv2.putText(frame,"yeniden konumlandir",(0,50),font,2,(0,0,255),2,lineType=cv2.LINE_AA)

    except:
        pass

    cv2.imshow("mask",mask)
    cv2.imshow("frame",frame)

    if cv2.waitKey(5) & 0xFF==ord("q"):

        break

vid.release()
cv2.destroyAllWindows()

    











    
