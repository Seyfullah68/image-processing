import cv2

resim=cv2.imread("klon.jpg")
#print(resim)
cv2.namedWindow("resimim",cv2.WINDOW_NORMAL) #resime cerceve ekler, buyultup kucultebiliriz
cv2.imshow("resimim",resim)
cv2.imwrite("kopya.jpg",resim) # kaydetme islemi
cv2.imwrite("E:\kopya.jpg",resim) # adreslerde turkce karakter olmamasina dikkat et
# gri=cv2.imread("klon.jpg",0) sifir parametresi ile resmi gri okur
cv2.waitKey(0)  #bir tusa basana kadar ekrani bekletir sifir yerine milisaniye degeride yazilabilir
cv2.destroyAllWindows()  #tum sekmeleri kapatir

