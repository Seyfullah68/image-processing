import face_recognition
import cv2


image=cv2.imread("face.jpg") # resmi import ettik

face_locations=face_recognition.face_locations(image)# yuzlerin koordinatlarini bulduk

print(face_locations)#yuzlerin koordinatlarini yazdirdik, ordaki degerlere gore dikdortgen cizdik

yuz1_1=(364,245)
yuz1_2=(454,335)

yuz2_1=(426,152)
yuz2_2=(533,259)

cv2.rectangle(image,yuz1_1,yuz1_2,(0,255,0))

cv2.rectangle(image,yuz2_1,yuz2_2,(0,255,0))


cv2.imshow("faces",image)
cv2.waitKey(0)

