import sympy
from sympy import sqrt
import math


a = symbols('a')

x = sympy.simplify((sqrt(a) - (a/sqrt(a)+1))*(a-1/sqrt(a)))
print(x)