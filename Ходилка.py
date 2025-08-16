WorldSize=(7)
def f(a):
    global WorldSize
    i=0
    j=0
    print("_____________")
    for i in range(WorldSize):
        for j in range(WorldSize):
            print(a[i][j],' ',end='',sep="")
        print()
        j=0
    print("_____________")

def help():
    print("команда \"0\" - Стоять")
    print("команда \"1\" - Вниз")
    print("команда \"2\" - ВВерх")
    print("команда \"3\" - Вправо")
    print("команда \"4\" - Влево")
    print("команда \"h\" - Вывод возможных действий")
    print("команда \"q\" - Конец игры")
print("Программа \"Ходилка\"")
print()
help()
print("_____________")
curI=0
curJ=0
i=0
a= [[0 for i in range(WorldSize)] for i in range(WorldSize)]
i=0
a[0][0]=1
print()
f(a)
while(1):
    print()
    o=input()
    if o==0:
        f(a)
    elif o=="1":
        a[curI][curJ]=0
        curI=curI+1
        a[curI][curJ]=1
        if (curI<0 or curI>WorldSize or curJ<0 or curJ>WorldSize):
            print("Вы вывалились за пределы карты.")
            break
        f(a)
    elif o=="2":
        a[curI][curJ]=0
        curI=curI-1
        a[curI][curJ]=1
        if (curI<0 or curI>WorldSize or curJ<0 or curJ>WorldSize):
            print("Вы вывалились за пределы карты.")
            break
        f(a)
    elif o=="3":
        a[curI][curJ]=0
        curJ=curJ+1
        a[curI][curJ]=1
        if (curI<0 or curI>WorldSize or curJ<0 or curJ>WorldSize):
            print("Вы вывалились за пределы карты.")
            break
        f(a)
    elif o=="4":
        a[curI][curJ]=0
        curJ=curJ-1
        a[curI][curJ]=1
        if (curI<0 or curI>WorldSize or curJ<0 or curJ>WorldSize):
            print("Вы вывалились за пределы карты.")
            break
        f(a)
    elif o=="q":
        break
    elif o=="h":
        help()
    else:
        print("не узнаю нужой команды")
print()
print("end")