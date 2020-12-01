import random
import matplotlib.pyplot as plt
x,y = 0.05 , 0
ordonne, abscisse = [],[]
for i in range(30000):
    p = random.uniform(0, 1)
    if p <= 0.02:
        xn = 0.5
        yn = 0.27 * y
    elif 0.02 < p <= 0.17:
        xn = -0.139 * x + 0.263 * y + 0.57
        yn = 0.246 * x + 0.224 * y - 0.036
    elif 0.17 < p <= 0.3:
        xn = 0.17 * x - 0.215 * y + 0.408
        yn = 0.222 * x + 0.176 * y + 0.0893
    else:
        xn = 0.781 * x + 0.034 * y + 0.1075
        yn = -0.032 * x + 0.739 * y  + 0.27
    x = xn
    y = yn
    abscisse += [xn]
    ordonne += [yn]
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse,ordonne,'r,')
plt.show