import numpy as np

#ndarray : n dimentional array

x=np.array([[1,2,3],[4,5,6]],np.int16)

print(x)#arrayin kendi
print(x.shape)#arrayin boyutlari(2,3)
print(x.ndim)#arrayin kac boyutlu oldugu(2)
print(x.size)#arrayde toplam eleman sayisi
print(x.dtype)#arrayin data turu
print(x.T)#arrayin transpozu(satirlar sutun,sutunlar satir oldu)