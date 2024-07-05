import cv2
import face_recognition

ronaldo=face_recognition.load_image_file("ronaldo.webp")#resmi okuduk

ornek_foto=cv2.imread("ornek.jpg")#resmi okuduk

ronaldo_encoding=face_recognition.face_encodings(ronaldo)[0]#ronaldonun yuzunun degerlerini belirledik,tek yuz oldugu icin 0 inci eleman
ornek=face_recognition.load_image_file("ornek.jpg")#ikinci fotoyu okuduk
ornekloc=face_recognition.face_locations(ornek)#ikinci fotodaki yuzun lokasyonlarini bulduk
ornek_encoding=face_recognition.face_encodings(ornek,ornekloc)#bu lokasyondaki yuzun degerlerini bulduk

karsilastirma=face_recognition.compare_faces(ronaldo_encoding,ornek_encoding)#iki fotodaki yuz degerlerini karsilastirdik

print(ornekloc)#ikinci fotodaki yuz degerlerinin lokasyonlarini yazdirip, degiskenlere atadik

x1=ornekloc[0][3]
x2=ornekloc[0][1]
y1=ornekloc[0][0]
y2=ornekloc[0][2]

if True in karsilastirma:#eger eslestirme uyuyorsa
    cv2.rectangle(ornek_foto,(x1,y1),(x2,y2),(0,255,0),2)#yuzun koordinatlarina dikdortgen cizdik
    print("trueee,eslesme bulunduu")
    cv2.putText(ornek_foto,"ronaldooo",(x1,y1),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),2)

else:
    print("eslesma bulunamadi..")



cv2.imshow("karsilastirma",ornek_foto)
cv2.waitKey(0)
cv2.destroyAllWindows()
