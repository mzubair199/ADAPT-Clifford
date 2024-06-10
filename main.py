import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return np.sin(x)

xx = np.linspace(0,6,50)

plt.plot(xx,fun(xx))
plt.show()