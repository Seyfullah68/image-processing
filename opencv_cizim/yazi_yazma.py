import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255

font1=cv2.FONT_HERSHEY_COMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX_SMALL
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"leo",(30,200),font3,5,(0,50,100),thickness=2)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
