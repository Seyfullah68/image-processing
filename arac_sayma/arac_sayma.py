import cv2 
import numpy as np

vid=cv2.VideoCapture("traffic.avi")# videoyu import ettik

arkaplan=cv2.createBackgroundSubtractorMOG2() # araka plan cikarmak icin tanimladik
sayac=0 # arac sayaci
while True:
    ret,frame=vid.read()
    if ret == False: # eger video biterse cikar
        break
    araclar=arkaplan.apply(frame) # araka plani cikardik, sadece araclar kaldi
    cv2.line(frame,(50,0),(50,300),(0,255,0),2) # ekrana iki tane cizgi cektik
    cv2.line(frame,(70,0),(70,300),(0,255,0),2)

    countours,hierarchi=cv2.findContours(araclar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# arabalarin contourlarini bulduk

    try : hierarchi=hierarchi[0]# daha az hata yapmak icin bunu yaptik
    except: hierarchi=[]

    for countor,hier in zip(countours,hierarchi): # zip ile yaptik(karsilikli tek tek tuple olusturur)

        (x,y,w,h) = cv2.boundingRect(countor)# countourlarin koordinat yukseklik ve genisligini bulduk

        if x>40 and h>40: # eger contourlar yeteri kadar buyuk ise
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) # countourlara dikdortgen cizdik
            if x>50 and x<70:# bizim sinirlardan gecerse sayaci bir arttirdik
                sayac+=1
        
        cv2.putText(frame,"car:"+str(sayac),(90,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2,cv2.LINE_AA)# araba sayisini yazdik


    cv2.imshow("arabalar",frame)
    cv2.imshow("araclar",araclar)

    if cv2.waitKey(40) & 0xFF== ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

