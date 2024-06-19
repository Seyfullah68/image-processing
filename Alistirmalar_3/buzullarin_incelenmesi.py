import cv2

img=cv2.imread("buzul.jpg")# resmi okuduk
cv2.imshow("orj",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#resmi gri ton a cevirdik
cv2.namedWindow("trackbar")#trackbarlar icin cerceve olusturduk

def bos(x):#bu fonksiyon trackbarlar icin gerekli
    pass

cv2.createTrackbar("lower","trackbar",0,255,bos)#tracbarlari olusturduk
cv2.createTrackbar("upper","trackbar",0,255,bos)

while True:

    lower=cv2.getTrackbarPos("lower","trackbar")#trackbarlarin degerilerini aldik
    upper=cv2.getTrackbarPos("upper","trackbar")

    ret,tresh=cv2.threshold(gray,lower,upper,cv2.THRESH_BINARY) #treshold u uyguladik

    cv2.imshow("treshold",tresh)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break
cv2.destroyAllWindows()
