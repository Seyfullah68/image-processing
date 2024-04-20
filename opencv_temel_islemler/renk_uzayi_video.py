import cv2

cap=cv2.VideoCapture("live.avi")

while True:
    ret,frame=cap.read() # ret video bitince false u dondurur, frame ise o anki ekrani alir
    if ret==False:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("live",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()