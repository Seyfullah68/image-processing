import cv2

img=cv2.VideoCapture(0)

while True:
    ret,frame=img.read()
    if ret==False:
        break
    frame=cv2.flip(frame,1)

    edges=cv2.Canny(frame,100,200)# bu fonk. ile kenarlari belirledik, min ve max degerleri girdik. 

    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

img.release()
cv2.destroyAllWindows()
