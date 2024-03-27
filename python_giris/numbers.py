# Type Conversion 

a=10
print(type(a))
print(a)
a=float(a)
print(type(a))
print(a)
a=complex(a)
print(type(a))
print(a)

# special methods

for i in range(2,5):
    print(i)
print("//////////\\\\\\\\\\")

for i in range(2,50,10):
    print(i)
print("//////////\\\\\\\\\\")

for i in range(50,2,-10):
    print(i)

listem=["a","ab","bcd"]
for i in range(len(listem)):
    print(listem[i])

print("//////////////////////////////")
import random

print(random.random()) # sifir ile bir arasinda rastgele sayi verir
print(random.randint(1,5)) # girilen degerler arasinda rastgele int sayi verir

print(abs(-55))# absolute - mutlak deger

import math
print(math.pi)
print(math.e)