import numpy as np

N = int(input("кол-во столбцов: "))
N1 = int(input("кол-во строчек: "))


a = np.zeros(shape=(N,N1))

for i in range(N):
    for j in range(N1):
        num = int(input())
        a[i,j]=(num)
    print("наибольшее число столбца № ")
    print(i)
    print(max(a[i]))

print(a)