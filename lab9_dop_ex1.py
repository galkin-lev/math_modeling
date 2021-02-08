
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 

y0=0

a=6
n = 7
u = 0
k = 1.05

def ap(a):
    a = k*a
    return a

def model(u,r):
    
    u = u + ap(a)
      
    dydt = u
    return dydt



r = np.arange(0,n)



y = odeint(model,y0,r)



# Построение решения в виде графика функции
plt.plot(r,y[:,0],y)
plt.xlabel('путь')
plt.ylabel('скорость')
plt.show()