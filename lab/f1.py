import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
x = np.sin(2 * np.pi * 1 * t)
plt.figure()
plt.grid()
plt.title("Continuous Time Signal")
plt.plot(t, x)
plt.show()
