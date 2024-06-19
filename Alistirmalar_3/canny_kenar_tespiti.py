import cv2

vid=cv2.VideoCapture(0) # videoyu kameradan aldik

while True:
    ret,frame=vid.read()

    frame=cv2.flip(frame,1)#goruntuyu y ekseninde cevirdik
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#goruntuyu gri tonlara cevirdik

    canny=cv2.Canny(gray,20,150)#kenarlari girilen treshold lara gore bulduk
    cv2.imshow("canny",canny)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
