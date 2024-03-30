import cv2

cap=cv2.VideoCapture(0) # kamera icin 0, pc deki video icin 1 parametresi girilir

while True:
    ret,frame=cap.read() # frame i dondurur, eger dogru ise ret dogru doner, yanlis ise ret false doner
    frame=cv2.flip(frame,1) # goruntuyu y ekseninde dondurur, 0 yazsaydik x ekseninde dondurur
    cv2.imshow("webcam",frame)
    if cv2.waitKey(30) & 0xFF == ord("q") :# her frame 30 milisaniye bekler ve klavyeden q harfine basilirsa break olur
        break
    
cap.relase()
cv2.destroyAllWindows()

"""cap=cv2.VideoCapture("video.mp4") # bilgisayarda kayitli video icin kullanilir

while True:
    ret,frame=cap.read() # frame i dondurur, eger dogru ise ret dogru doner, yanlis ise ret false doner
    if ret == 0: # video bitince frame olmaz ve ret sifir doner
        break
    frame=cv2.flip(frame,1) # goruntuyu y ekseninde dondurur, 0 yazsaydik x ekseninde dondurur
    cv2.imshow("webcam",frame)
    if cv2.waitKey(30) & 0xFF == ord("q") :# her frame 30 milisaniye bekler ve klavyeden q harfine basilirsa break olur
        break
    
cap.relase()
cv2.destroyAllWindows()"""