import numpy as np
import matplotlib.pyplot as plt

mnd = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # [mnd nr]
temp = np.array([-3, -2, 2, 7, 11, 15, 17, 16, 12, 6, 2, -3])  # [C]

plt.plot(mnd, temp)
plt.show()