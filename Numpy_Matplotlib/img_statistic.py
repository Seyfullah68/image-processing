import matplotlib.pyplot as plt
import numpy as np

img=plt.imread("C:\\Users\\seyfu\\Downloads\\smile.jpg")

print(img)
print("min:",img.min())
print("max:",img.max())
print("mean:",img.mean())
print("avarage:",np.average(img))
print("mean2:",np.mean(img))
print("median",np.median(img))
