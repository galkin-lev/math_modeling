def midlevalue(a):
    x = 0
    for i in a:
        x = x+i
    if (a!=0):
        mid = x/len(a)
        return mid

a = [2,4,6]
print(midlevalue(a))