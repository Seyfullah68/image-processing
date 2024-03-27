
# while loop
"""counter =0

while counter<=10:
    print(counter)
    counter +=1"""

# for loop

liste=[1,2,3,4]
liste2=["a","b","c"]
for i in liste:
    print(i)
for i in liste2:
    print(i)

for i in "leo":
    print(i)

for i in liste:
    print("i:",i)
    for j in ["a","aa","aaa"]:
        print("j:",j)
print("////////////////////////////")

#continue and pass

for i in "apachi":
    if i=="c":
        continue
    print(i)

print("////////////////////////////")

for i in "apachi":
    if i=="c":
        pass
    print(i)

print("////////////////////////////")

for i in "apachi":
    if i =="c":
        break
    print(i)


