x = int(input("Введите число:"))
m = 0
while x>0:
    m = m*10 + x%10
    x = x//10
print("Значение = " + str(m))