import cv2
import numpy as np
# morphology kutuphanesine opencv kutuphanesinden bak! Ornekler daha aciklayici
img=cv2.imread("heli.webp",0)
kernel=np.ones((5,5),dtype=np.uint8)# matris boyutu arttikca goruntu daha da bozulur
erezyon=cv2.erode(img,kernel,iterations=1)# iterasyon tekrar sayisi, arttirdikca goruntu daha da bozulur

kalinlasma=cv2.dilate(img,kernel,iterations=5)

# erezyonda siyahlar uzerinden, kalinlasmada beyazlar uzerinden bozulma yapilir

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("orj",img)
cv2.imshow("erezyon",erezyon)
cv2.imshow("kalinlastirma",kalinlasma)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
