import cv2

vid=cv2.VideoCapture(0)

cv2.namedWindow("live")

print("width:"+str(vid.get(3))) # get(3) goruntunun genisligini verir
print("height:"+str(vid.get(4)))# get(4) goruntunun yuksekligini verir

vid.set(3,1280) # goruntunun genisligini degistirdik
vid.set(4,720) # goruntunun yuksekligini degistirdik

print("width_son:"+str(vid.get(3)))
print("height_son:"+str(vid.get(4)))
while True:
    ret,frame=vid.read()

    frame=cv2.flip(frame,1)

    cv2.imshow("live",frame)

    if cv2.waitKey(1)==27: # 27:esc asci kodu
        break

vid.release()
cv2.destroyAllWindows()