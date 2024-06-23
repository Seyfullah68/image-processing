import matplotlib.pyplot as plt
import numpy as np

x=np.arange(5)
y=x

plt.plot(x,y)

plt.plot(x,-y,"o")

plt.plot(-x,y,"o--")
plt.title("x=y,x=-y,-x=y")
plt.show()
