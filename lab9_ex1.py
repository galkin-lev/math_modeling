
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 

 
def model(y,t):
    k = 0.5

    dydt = k * y
    return dydt

y0=1

t = np.arange(0,6)



y = odeint(model,y0,t)



# Построение решения в виде графика функции
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('количество бактерий')
plt.show()
