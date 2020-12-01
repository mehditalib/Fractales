import random
import matplotlib.pyplot as plt
a1,b1 = 1,1
a2,b2 = 2,2
a3,b3 = 3,1
x0,y0 = 2,1.5
ordonne, abscisse = [],[]
for i in range(15000):
    p = random.uniform(0, 1)
    if p <0.333:
        xn = (x0+a1)/2
        yn = (y0+b1)/2
    elif 0.333<= p < 0.666:
        xn = (x0+a2)/2
        yn = (y0+b2)/2
    else:
        xn = (x0+a3)/2
        yn = (y0+b3)/2
    x0 = xn
    y0 = yn
    abscisse += [xn]
    ordonne += [yn]
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse,ordonne,'r,')
plt.show