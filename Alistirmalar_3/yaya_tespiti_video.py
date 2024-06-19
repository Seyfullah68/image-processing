import cv2
import imutils

img=cv2.VideoCapture("yaya.mp4") # videoyu okuduk


while True:

    ret,frame=img.read()

    frame=imutils.resize(frame,250)# resmi tekrardan boyutlandirdik


    hog=cv2.HOGDescriptor() # bu fonskiyonu hog degiskenine atadik
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())#yaya algilama class ini bu degiskene. uyguladik

    (korninat,a)=hog.detectMultiScale(frame,winStride=(4,4),padding=(8,8),scale=1.05)#yayalarin koordinatlarini aldik

    print(korninat)


    for (x,y,w,h) in korninat:# bulunan koordinatlara dikdortgen cizdik
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow("img",img)
    if cv2.waitKey(20) & 0XFF==ord("q"):
        break

img.release()
cv2.destroyAllWindows()