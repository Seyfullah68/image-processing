import cv2
import numpy as np

bit1=cv2.imread("bitwise_1.png")
bit2=cv2.imread("bitwise_2.png")
# bitwise karsilikli bitleri karsilastirir, siyah 0, beyaz 1 dir.
bitwise_and=cv2.bitwise_and(bit1,bit2)# and operatoru ile karsilastirma yapilir.
bitwise_or=cv2.bitwise_or(bit1,bit2)
bitwise_xor=cv2.bitwise_xor(bit1,bit2)
bitwise_not1=cv2.bitwise_not(bit1)
bitwise_not2=cv2.bitwise_not(bit2)

cv2.imshow("bit1",bit1)
cv2.imshow("bit2",bit2)
cv2.imshow("bitwise_and",bitwise_and)
cv2.imshow("bitwise_or",bitwise_or)
cv2.imshow("bitwise_xor",bitwise_xor)
cv2.imshow("not1",bitwise_not1)
cv2.imshow("not2",bitwise_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()
