import cv2

def bos(x):
    pass

cv2.namedWindow("donusum")
img1=cv2.imread("aircraft.jpg")
img1=cv2.resize(img1,(640,480))

img2=cv2.imread("starwars.jpg")
img2=cv2.resize(img2,(640,480))

output=cv2.addWeighted(img1,0.5,img2,0.5,0)# resimleri agirlikli olarak birbirine ekledik. 0 degeri sabit.

cv2.createTrackbar("alpha-beta","donusum",0,1000,bos)

while True:
    alpha=cv2.getTrackbarPos("alpha-beta","donusum")/1000 # 1000 e bolduk cunku 0-1 arasinda deger alir.
    beta=1-alpha # alpha ve betanin toplami herzaman 1 dir.

    output=cv2.addWeighted(img1,alpha,img2,beta,0)

    cv2.imshow("donusum",output)
    if cv2.waitKey(5)==27:
        break

cv2.destroyAllWindows()