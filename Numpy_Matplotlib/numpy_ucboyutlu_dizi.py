import numpy as np

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],np.int16)

print(x)
print("-----")
print(x[0]);print(x[0,:,:])
print("-----")
print(x[0,0,1])
print(x[1,0,2])
print("-----")
print(x[1,1])
