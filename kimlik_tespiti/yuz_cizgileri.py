import face_recognition
from PIL import Image,ImageDraw

image=face_recognition.load_image_file("face.jpg")# resmi import ettik

landmarks=face_recognition.face_landmarks(image)#yuz cizgilerinin koordinatlarini bulduk

PIL=Image.fromarray(image)#bu islemleri gorsele cizgi cizmek icin yaptik
d=ImageDraw.Draw(PIL)


for landmark in landmarks:#koordinatlari teker teker gezdik
    for key in landmark.keys():#dizi elemanlari sozluk, biz key degerlerini aldik
        d.line(landmark[key],width=3)#key degerlerini gorsele cizdik
    
PIL.show()#resmi gosterdik
