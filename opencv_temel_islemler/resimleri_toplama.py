import cv2
import numpy as np

cember= np.zeros((512,512,3),dtype=np.uint8)+255
cv2.circle(cember,(256,256),60,(255,0,0),thickness=-1)

dortgenim=np.zeros((512,512,3),dtype=np.uint8)+255
cv2.rectangle(dortgenim,(150,150),(350,350),(0,0,255),thickness=-1)
toplam=cv2.add(cember,dortgenim)
cv2.imshow("dortgen",dortgenim)
cv2.imshow("cemberim",cember)
cv2.imshow("toplam",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()