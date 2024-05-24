import cv2

vid=cv2.VideoCapture(0)

circle=[]
def mouse(event,x,y,flags,params): # mouse icin olusturduk. x ve y noktanin koordinatlari. event yapilan islem. digerleri olmasi gerekiyor
    
    if event == cv2.EVENT_LBUTTONDOWN: # eger mouse un left button u down ise, yani sol taraf basilmissa
        circle.append((x,y))# listeye koordinatlari ekledik

cv2.namedWindow("frame")

cv2.setMouseCallback("frame",mouse)# mouse u bu pencereye set ettik.

while 1:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)

    for crc in circle:
        cv2.circle(frame,crc,10,(0,0,255),-1) # koordinatlari alip daire cizdik

    cv2.imshow("frame",frame)

    key=cv2.waitKey(1) # bir tusa basmak icin tanimladik

    if key==27: # esc ise sonlandir
        break
    elif key==ord("c"): # c ise circle i temizledik
        circle=[]
    

vid.release()
cv2.destroyAllWindows()


