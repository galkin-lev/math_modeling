  
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60

years = 2

t = np.arange(0, years*seconds_in_year, seconds_in_day)
              
              
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = 149 * 10**9
v_x20 = 1
y20 = 0
v_y20 = -30000

x30 = 0
v_x30 = 15000
y30 = 149 * 10**9
v_y30 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

m1 = 1.1 * 10**(30)
q1 = -1.1 *10**(20)

m2 = 2.1 * 10**(30)
q2 = 2.1 *10**(20)

m3 = 3.6 * 10**(30)
q3 = -3.1 *10**(20)



def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s

    dxdt1 = v_x1
    dv_xdt1 = (
               - G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               - G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
                )
    dydt1 = v_y1
    dv_ydt1 = (
               - G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               - G * m2 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
                )

    dxdt2 = v_x2
    dv_xdt2 = (
               - G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               - G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
                )
    dydt2 = v_y2
    dv_ydt2 = (
               - G * m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               - G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
                )
    dxdt3 = v_x3
     
    dv_xdt3 = (
               - G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               - G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
    
    dydt3 = v_y3
    dv_ydt3 = (
               - G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               - G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               + k * q3 * q2 / m3 * (x3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
                )
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)
    
    
    

sol = odeint(move_func, s0, t)    
    

    # Определяем начальные значения и параметры


#m2 = 1.98 * 10**(30)
#s0 = (x10, v_x10, y10, v_y10,
#      x20, v_x20, y20, v_y20)



#def f1(x1, x2, y1, y2, m):
 #   return (-G * m * (x2 - x1)/((x2-x1)**2 +(y2-y1)**2)**1.5)

#def f2(x1, x2, y1, y2,q1,q2, m):
#    return ()

#def formula(x1, x2, x3, y1, y2, y3, m1, m2, m3, q1, q2, q3):
#    return (f1(x1,x2,y1,y2,m)+f1(x3,x2,y3,y2,m3))





fig = plt.figure()
bodys = []

for i in range(0, len(t), 1):
    body1, = plt.plot(sol[:i,0], sol[:i, 2], '-', color='g')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='g')
    
    body2, = plt.plot(sol[:i,4], sol[:i, 6], '-', color='g')
    body2_line, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='g')
    
    body3, = plt.plot(sol[:i,8], sol[:i, 10], '-', color='g')
    body3_line, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='g')

# Строим решение в виде графика и анимируем

    
ani = FuncAnimation(fig, bodys, interval=50)

plt.axis('equal')

ani.save('The_result_of_the_Coulomb_experiment.gif', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
