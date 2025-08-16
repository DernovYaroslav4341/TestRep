a=7*[0]
i=0
print("введи семь цифр")
for i in range(7):
    print(a)
    a[i]=input()
for i in range(7):
    print("ВВедёная цыфра номер ",i,": ",a[i],sep="")
print("end")