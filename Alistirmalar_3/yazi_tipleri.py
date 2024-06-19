import cv2
import numpy as np

"""
cv2.FONT_HERSHEY_SIMPLEX:0
cv2.FONT_HERSHEY_PLAIN:1
cv2.FONT_HERSHEY_DUPLEX:2
cv2.FONT_HERSHEY_COMPLEX:3
cv2.FONT_HERSHEY_TRIPLEX:4
cv2.FONT_HERSHEY_COMPLEX_SMALL:5
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX:6
cv2.FONT_HERSHEY_SCRIPT_COMPLEX:7
"""

screen=np.ones((800,500),dtype=np.uint8)*255 #beyaz bir ekran olusturduk

text="open cv"
color=(100,0,80)

for i in range(8):
    cv2.putText(screen,text,(50,50+i*50),i,3,color,3)#yazilari yazdik

cv2.imshow("text",screen)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

