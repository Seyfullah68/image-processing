# haar cascade insan vucudu algilamada basarili olmadigi gibi arac algilamada da basarili degildir. 
# cunku farkli sekil ve renklerde araclar vardir

import cv2

img=cv2.imread("car.jpg")

car_cascade=cv2.CascadeClassifier("car.xml")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cars=car_cascade.detectMultiScale(gri,1.2,1)

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("cars",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
