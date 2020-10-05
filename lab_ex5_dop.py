i = int(input("Введите число:"))
x = 1
sum = 0;
while x<i:
    if i%x == 0:
        sum +=x
        x+=1
    else:
        while i%x != 0:
            x+=1
            if x == i:
                break
        if x == i:
            break

if i == sum:
    print("Число совершенно")
else:
    print("Число несовершенно")