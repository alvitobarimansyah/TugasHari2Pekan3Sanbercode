import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
cos = np.cos(x)
cos3 = np.cos(x)*3
sin = np.sin(x-90)
sin2 = np.sin(x)*2

fig, ax = plt.subplots()

ax.plot(x, cos, color = 'red' , label = 'Cosx')
ax.plot(x, cos3, linestyle = '--', color = 'green', label = '3 Cosx')
ax.plot(x, sin, linestyle = '-.', color = 'blue', label = 'Sin(x-90)')
ax.plot(x, sin2, marker = 'x', linestyle = '', color = 'yellow', label = '2 Sinx')

ax.legend(loc = 'center')
ax.set_xlabel('X-Axis Label')
ax.set_ylabel('Y-Axis Label')
ax.set_title('Grafik Cos Sin')

plt.show()