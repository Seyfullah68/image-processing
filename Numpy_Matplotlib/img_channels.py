import matplotlib.pyplot as plt

img=plt.imread("C:\\Users\\seyfu\\Downloads\\map.jpg")#plt her zaman rgb olarak okur

r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]

output=[img,r,g,b]
#output=np.dstack((r,g,b)) : bu fonk. r,g ve b yi birlestirerek orj img yi elde etmemizi saglar
titles=["img","red","green","blue"]
for i in range(4):
    plt.subplot(2,2,i+1)#2 ye 2 lik gorsel tablosunun i+1 inci bolumunde goster demek
    plt.axis("off")
    plt.title(titles[i])

    if i==0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap="gray")

plt.show()