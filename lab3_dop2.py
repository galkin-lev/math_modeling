a = []
N = 5
for i in range(N-1):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))

if (j<=N and j>=0):
    a.insert(j-1,num)

print(a)