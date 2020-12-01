import random
import matplotlib.pyplot as plt
x,y = 0.5 , 0
ordonne, abscisse = [],[]
for i in range(30000):
    p = random.uniform(0, 1)
    if p<0.1:
        xn = 0.05 * x
        yn = 0.60 * y
    elif 0.1 <= p < 0.2:
        xn = 0.05 * x
        yn = -0.5 * y + 1
    elif 0.2 <= p < 0.4:
        xn = 0.46 * x - 0.32 * y
        yn = 0.39 * x + 0.38 * y + 0.6
    elif 0.4 <= p < 0.6:
        xn = 0.47 * x - 0.15 * y
        yn = 0.17 * x + 0.42 * y + 1.1
    elif 0.6 <= p < 0.8:
        xn = 0.34 * x + 0.28 * y
        yn = -0.25 * x + 0.45 * y + 1
    else:
        xn = 0.42 * x + 0.26 * y
        yn = -0.35 * x + 0.31 * y + 0.70
    x = xn
    y = yn
    abscisse += [xn]
    ordonne += [yn]
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse,ordonne,'g,')
plt.show