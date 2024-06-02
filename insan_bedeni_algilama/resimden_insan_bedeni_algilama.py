import cv2
# haar cascade ile insan bedeni algilamak zor, cunku farkli sekil ve gorunuslerde insan bedenleri vardir.
#bu yuzden daha farkli bir yol kullanilir.(araclar icinde aynisi gecerlidir)

img=cv2.imread("body.jpg")

body_cascade=cv2.CascadeClassifier("fullbody.xml") # haar cascade vucut dosyasini import ettik

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# resmi gri ton a cevirdik

body=body_cascade.detectMultiScale(gray,1.3,4)# resimde vucutlarin koordinatlarini bulduk

for (x,y,w,h) in body: # bulunan koordinatlara dikdortgen cizdik
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()