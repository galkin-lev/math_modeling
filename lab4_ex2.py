import numpy as np

def a(a):
    a = np.prod(np.array(a))  
    return a

mylist = [4,6,7]
print(a(mylist))