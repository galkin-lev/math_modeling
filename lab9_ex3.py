
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 

y0=10
u=0
a0=2
n = 8


def model(u,t):
    k = 0.01
    u = u + a0

    r = k*(u**2/t)
    dydt = u - r
    return dydt



t = np.arange(1,n)



y = odeint(model,y0,t)



# Построение решения в виде графика функции
plt.plot(t,y[:,0],y)
plt.xlabel('time')
plt.ylabel('скорость')
plt.show()