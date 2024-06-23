import numpy as np
import matplotlib.pyplot as plt

"""n=11
x=np.linspace(0,10,n)#sifir ile 10 arasinda n kadar sayi uretir
print(x)
y=x
plt.plot(x,y,"o")
plt.axis("off")#eksenleri kaldirdik
plt.show()"""

x=[1,2,3,4]
plt.plot(x,[y**3 for y in x])
plt.show()