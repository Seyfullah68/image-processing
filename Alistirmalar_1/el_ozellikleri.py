import cv2
import numpy as np
import math

def maxcontour(kontur):

    max_area=0
    max_i=0

    for i in range(len(kontur)):

        area=cv2.contourArea(kontur[i])
        
        if area>max_area:
            max_area=area
            max_i=i
        
        # eger kontur varsa bu try islemi yapilir, yoksa bu deger except islemi yapilir
            try:
                c=kontur[i]
        
            except:
                kontur=[0]
                c=kontur
    
    return c
        


vid=cv2.VideoCapture(0)

while 1:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)

    roi=frame[50:300,200:400]# [y1:y2,x1:x2] # videoda kirpilacak bolumun koordinatlari

    cv2.rectangle(frame,(200,50),(400,300),(0,0,255),0)# kirpilan bolume dikdortgen ekledik, mask islemine dahil olmamasi icin kalinligi 0

    hsv= cv2.cvtColor(roi,cv2.COLOR_BGR2HSV) # kirpilacak kismi hsv formatina cevirdik
    lower=np.array([0,45,79], dtype=np.uint8) # bu degerleri internetten aldik
    upper=np.array([17,255,255],dtype=np.uint8)

    

    mask=cv2.inRange(hsv,lower,upper) # mask uyguladik
    kernel=np.ones((3,3),dtype=np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1) # beyazliklari kalinlastirtik
    mask=cv2.medianBlur(mask,15) # netlestirme yaptik

    conturs,a=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(conturs)>0: # eger kontur varsa 

        
        c=maxcontour(conturs) # fonksiyonu ustte tanimladik
        en_sol=tuple(c[c[:,:,0].argmin()][0]) # konturlarin en sag, en sol ve en ust noktalarini bulduk
        en_sag=tuple(c[c[:,:,0].argmax()][0])
        en_ust=tuple(c[c[:,:,1].argmin()][0])
        

        cv2.circle(roi,en_sol,5,(0,255,0),2)
        cv2.circle(roi,en_sag,5,(0,255,0),2)
        cv2.circle(roi,en_ust,5,(0,255,0),2)
        
        cv2.line(roi,en_sol,en_ust,(255,0,0),2)
        cv2.line(roi,en_ust,en_sag,(255,0,0),2)
        cv2.line(roi,en_sag,en_sol,(255,0,0),2)

        # aci bulmak icin uzunluklari hesapladik
        a=math.sqrt((en_sag[0]-en_ust[0])**2+(en_sag[1]-en_ust[1])**2)
        b=math.sqrt((en_sag[0]-en_sol[0])**2+(en_sag[1]-en_sol[1])**2)
        c=math.sqrt((en_ust[0]-en_sol[0])**2+(en_ust[1]-en_sol[1])**2)

        try: # eger aci bulunursa bu islem yapilir
            angle=int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)

            cv2.putText(roi,str(angle),(en_sag[0]-50,en_sag[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
            if angle>70: # aci 70 dereceden buyukse asagidaki islemler yapilir

                cv2.rectangle(frame,(0,0),(50,50),(255,0,0),-1)
            else:
                pass


        except: # eger aci bulunamazsa bu islem yapilir
            cv2.putText(roi,"yok",(en_sag[0]-50,en_sag[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))




        


    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
