import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
 

y0=0

s = 1600

n = 12

k = 1.5

def get_degrees(t):
    
     if t == 0:
        return float(math.degrees(math.cos(math.radians(0))))
     elif t == 1:
        return float(math.degrees(math.cos(math.radians(15))))
     elif t == 2:
        return  float(math.degrees(math.cos(math.radians(30))))
     elif t == 3:
        return float(math.degrees(math.cos(math.radians(45))))
     elif t == 4:
        return float(math.degrees(math.cos(math.radians(60))))
     elif t == 5:
        return float(math.degrees(math.cos(math.radians(75))))
     elif t == 6:
        return float(math.degrees(math.cos(math.radians(90))))
     elif t == 7:
        return  float(math.degrees(math.cos(math.radians(75))))
     elif t == 8:
        return float(math.degrees(math.cos(math.radians(60))))
     elif t == 9:
        return float(math.degrees(math.cos(math.radians(45))))
     elif t == 10:
        return float( math.degrees(math.cos(math.radians(30))))
     elif t == 11:
        return float(math.degrees(math.cos(math.radians(15))))
     elif t == 12:
        return float(math.degrees(math.cos(math.radians(0))))
    
     
   

    
a = 6
d = 0
    


def model(s,t):
    
    s = s + k*s*float(get_degrees(t))
      
    dydt = s
    return dydt



t = np.arange(0,12)




y = odeint(model,s,t)



# Построение решения в виде графика функции
plt.plot(t,y[:,0],y)
plt.xlabel('путь')
plt.ylabel('скорость')
plt.show()