import numpy as np
import matplotlib.pyplot as plt

x=np.arange(5)
print(x)

plt.plot(x,[y**2 for y in x])
plt.plot(x,[y**3 for y in x])
plt.plot(x,x*2)
plt.plot(x,x+5)
plt.legend(["x**2","x**3","2*x","x+5"],loc="upper center")#cizgilerin isimlerini ust orta locasyona yazdik
plt.grid(True)# grafikte kare bolmeleri aktif ettik
plt.title("simple graph")#grafige isim verdik
plt.xlabel("x ekseni")#eksenlere isim verdik
plt.ylabel("y ekseni")
print(plt.axis())# grafikte min ve max noktalari verir
plt.axis([0,4,0,60])#grafigin eksen boyutunu verilere gore duzenledik
plt.savefig("graph.jpg")#grafigi kaydettik
plt.show()