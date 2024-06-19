from PIL import Image  # kutuphaneleri import ettik
import pytesseract

img=Image.open("ornek.jpg") #resmi actik

yazi=pytesseract.image_to_string(img,lang="eng")#resmi yaziya cevirdik

print(yazi)

with open("dosya.txt",mode="w") as file: # dosya.txt seklinde, write modunda dosya actik
    file.write(yazi) # dosya ya yaziyi yazdik

print("islem tamam!")
