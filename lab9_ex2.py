

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 

 
def model(y,t):
    k = 0.08

    dydt = -k * y * t
    return dydt

y0=1000


n = 4

t = np.arange(0,n)



y = odeint(model,y0,t)



# Построение решения в виде графика функции
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('количество бактерий')
plt.show()
