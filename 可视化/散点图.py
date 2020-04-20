import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 20)
y = np.random.normal(0, 1, 20)

x1 = np.random.normal(0, 1, 20)
y1 = np.random.normal(0, 1, 20)
plt.figure()
plt.scatter(x, y, s=150, label='luv')
plt.scatter(x1, y1, label='hon')
plt.legend()
plt.show()
