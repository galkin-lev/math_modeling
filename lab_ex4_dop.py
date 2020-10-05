i = int(input("Введите число:"))
x = 2
while i>0:
    if i%x == 0:
        i=i/x
        print(x)
        x = 2
    else:
        while i%x != 0:
            x+=1
    if i == 1:
        print(1)
        break;