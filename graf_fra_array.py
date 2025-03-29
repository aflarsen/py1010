# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:43:42 2024

@author: AFL015
"""

import numpy as np

x = 2.0
y = np.sqrt(x)

print('x =', x)
print('y =', y)


#####


import numpy as np
import matplotlib.pyplot as plt

mnd = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # [mnd nr]
temp = np.array([-3, -2, 2, 7, 11, 15, 17, 16, 12, 6, 2, -3])  # [C]

plt.plot(mnd, temp)
plt.show()