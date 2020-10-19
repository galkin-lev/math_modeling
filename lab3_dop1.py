import numpy as np
n=4
p=3
a = np.zeros(shape=(n, p))
for (i,j), x in np.ndenumerate(a):
    print( i,j, x,sep = "; ")
    m = input (f"введите значение массива [i,j]: ")
    a[i,j] = float (m)
print(a)
a2 = np.zeros(shape=(n, p))
for (i,j), x in np.ndenumerate(a2):
    print( i,j, x,sep = "; ")
    m = input (f"введите значение массива [i,j]: ")
    a2[i,j] = float (m)
print(a2)
a3 = np.zeros(shape=(n, p))
for(i,j), x in np.zeros(shape=(n,p)):
    if a[i,j]>a2[i,j]:
        a3[i,j]=a[i,j]
    else:
        a3[i,j] = a2[i,j]
        