import cv2

cap = cv2.VideoCapture(0)
filename="E:\live.avi" # adres ve video ismi
codec= cv2.VideoWriter_fourcc('W','M','V','2')# codec ses goruntu birlesmesidir, avi icin bu degerler girilir
frameRate=30 # frame hizi
resolution=(640,480)# cozunurluk
videokayit=cv2.VideoWriter(filename,codec,frameRate,resolution)
while True:
    ret,frame = cap.read()
    frame= cv2.flip(frame,1)
    videokayit.write(frame) # video, dosyaya yazilir
    cv2.imshow("live",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

videokayit.release()
cap.release()
cv2.destroyAllWindows()