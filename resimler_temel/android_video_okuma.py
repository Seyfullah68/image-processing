import cv2
import numpy as np
import requests

url="-----\shot.jpg" # site uzerindeki videonun anlik ss i 

while True:
    img_resp=requests.get(url) # ss leri url den aldik
    img_arr= np.array(bytearray(img_resp.content),dtype=np.uint8) # alinan ss leri bytearray olarak seride tuttuk
    img= cv2.imdecode(img_arr,cv2.IMREAD_COLOR) # renkleri ve diziyi img ye atadik

    img= cv2.resize(img,(640,480))
    cv2.imshow("android_kamera",img)
    if cv2.waitKey(1)==27:  # esc ye basinca cikis yapar
        break

cv2.destroyAllWindows()