import cv2
import numpy as np

cember= np.zeros((512,512,3),dtype=np.uint8)+255
cv2.circle(cember,(256,256),60,(255,0,0),thickness=-1)

dortgenim=np.zeros((512,512,3),dtype=np.uint8)+255
cv2.rectangle(dortgenim,(150,150),(350,350),(0,0,255),thickness=-1)
agirlikli=cv2.addWeighted(cember,0.8,dortgenim,0.2,0)# yuzde agirliklarini girdik, sondaki sifir ile en sonunda toplanir goruntu
cv2.imshow("dortgen",dortgenim)
cv2.imshow("cemberim",cember)
cv2.imshow("addweighted",agirlikli)

cv2.waitKey(0)
cv2.destroyAllWindows()