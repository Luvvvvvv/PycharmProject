import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y, label='LUV', color='red')
plt.plot(x, y2, label='HON', color='black')
plt.legend()

plt.xlabel('HON')
plt.ylabel('LUV')

plt.show()
