import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8)
canvas+=255

cv2.line(canvas,(50,50),(512,300),(255,0,0),thickness=5)
cv2.line(canvas,(70,10),(70,512),(0,0,255),thickness=7)

cv2.rectangle(canvas,(8,10),(80,100),(0,255,0),thickness=2)
cv2.rectangle(canvas,(0,0),(50,50),(30,80,200),thickness=-1) # -1 olunca icini dolu yapar
cv2.circle(canvas,(256,256),(50),(5,200,255),thickness=-1)
# ucgen olusturma

p1=(100,100)
p2=(180,160)
p3=(120,50)
cv2.line(canvas,p1,p2,(0,0,0),thickness=4)
cv2.line(canvas,p2,p3,(0,0,0),thickness=4)
cv2.line(canvas,p3,p1,(0,0,0),thickness=4)

points=np.array([[150,70],[190,150],[400,300],[500,470]],dtype=np.int32)
cv2.polylines(canvas,[points],True,(0,100,200),thickness=5)# true girince kapali bir sekil olusturur.

cv2.ellipse(canvas,(400,400),(10,50),100,90,360,(255,80,80),thickness=-1)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
