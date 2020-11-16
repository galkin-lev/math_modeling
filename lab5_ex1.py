import math

a = int(input("введите косинус"))
b = int(input("введите синус"))
anum = int(input("введите число а"))

def absd(a,b,anum):

    cosh = math.cosh(a)
    sinh = math.sinh(b)
    cos = math.cos(a)
    sin = math.sin(b)

    x = anum*sinh/cosh-cos
    y = anum*sin/cosh-cos

    print(x)
    print(y)
    
print(absd(a,b,anum))