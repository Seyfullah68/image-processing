from PIL import Image # python image library den image i import ettik

import pytesseract # pytesseract i import ettik

img=pytesseract.image_to_string("text.png",lang="eng")# resmi okuyup,string e cevirdik

print(img)
