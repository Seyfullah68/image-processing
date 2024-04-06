import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) # 3 kanalli olusturduk ve data tipini uint8 kullaniriz
print(canvas)

cv2.imshow("canvas_black",canvas)

canvas+=255
cv2.imshow("canvas_white",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()