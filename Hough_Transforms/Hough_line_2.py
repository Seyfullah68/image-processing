import cv2
import numpy as np

vid=cv2.VideoCapture("line.mp4")
while True:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,480))# frame i tekrardan boyutlandirdik
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # goruntuyu hsv formatina cevirdik

    # hsv formatinda sari cizgi degerlerini internetten bulduk. hsv range for yellow

    lower=np.array([18,94,140],dtype=np.uint8)
    upper=np.array([48,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,lower,upper) # sari serit i filtreledik
    edges=cv2.Canny(mask,75,255)# filtrelenen kisimin kenarlarini belirledik
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)#kenarlara gore cizgi cizdik
    for line in lines:
        x1,y1,x2,y2=line[0] # cizginin baslangic ve bitis koordinatlari
        cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),5)



    cv2.imshow("frame",frame)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()