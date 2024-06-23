import numpy as np

x=np.empty((3,2),dtype=np.uint16) # bos matris  ve uint demek(unsigned integer) negatif sayi olamamasidir
print("x:",x)
print("------")

y=np.full((2,1,3),fill_value=7,dtype=np.uint16)
print("y:",y)
print("------")

z=np.ones((2,1,4),np.uint16)
print("z:",z)
print("------")

w=np.zeros((3,1,2),np.uint16)
print("w:",w)