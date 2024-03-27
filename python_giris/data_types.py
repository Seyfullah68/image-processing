# Numeracial Types

x=5
print("x:{}, tipi:{}".format(x,type(x)))
y=5.5
print("y:{}, tipi:{}".format(y,type(y)))
z=5+5j
print("z:{}, tipi:{}".format(z,type(z)))

print("**********************")
# Strings
mesaj="naber dunya"
print(mesaj)
print(mesaj[4])
print(mesaj[2:6])
print(mesaj[2:])
print(mesaj[:5])
print(mesaj+"5")
#print(mesaj+5)  : type error
#print(mesaj+str(5)) : solution

print("**********************")
# lists

liste=[10,"apachi",-5,7.4]
print(liste[:3])
print("**********************")
#Tuple
tuplem=(10,"aa",4.4)
print(tuplem[1:])

print("**********************")
# Dictionary 

sozluk={"name":"seyfo",
        "surname":"ilgun",
        "age":26}
print(sozluk)
print(sozluk["name"])
print(sozluk["surname"])
print(sozluk["age"])
print(sozluk.keys())
print(sozluk.values())

print("**********************")
# Boolean

x=True
y=False
z=None
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
