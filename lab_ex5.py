a = float(input("первое число"))
b = float(input("второе число"))
if b == 0:
    print("ошибка деления на 0")
elif a%b != 0  : 
    print(a//b)
    print("остаток" + str(a%b) )
else: 
    print("значение = " + str(a//b))