from matptotlib import pyplot as plt
import numpy as np


def systema(x):
    return x**2 + 23


x = np.linspace(-10, 10, 400)

y = systema(x)
plt.plot(x, [systema(x) for x in x])
plt.show()
