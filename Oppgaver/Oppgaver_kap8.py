# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 16:46:41 2025

@author: AFL015

Oppg kap 8

"""

#%% Oppg 8.1

for i in range(5,36):
    print(i)
    
#%% Oppg 8.2

for i in range(105, 36, -2):
    print(i)
    
#%% Oppg 8.3

y = 0

for i in range(14, 109):
    if i % 2 == 0:
        # print(i)
        y += i
        
print(y)

#%% Oppg 8.4

for i in range(5, 36):
    if i == 24:
        print("fireogtyve")
    else:
        print(i)
        
#%% Oppg 8.5

import numpy as np

arr = np.zeros(31)

for i in range(5, 36):
    arr[i - 5] = 1 / i

print(arr)

#%% Oppg 8.6

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 20)

def f(x):
    return np.sin(x)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')

for x_val in x:
    print('For x =', round(x_val, 5), ' er f(x) =', round(f(x_val), 5))

#%% Oppg 8.7

import numpy as np

def my_linspace(start, stop):
    antall = 50
    dx = (stop-start)/(antall-1)
    x1 = start
    arr = np.zeros(antall)

    for i in range(0, antall):
        arr[i] = x1
        x1 = x1+dx

    return(arr)

print('fasit =', np.linspace(1, 7))
print('my_linspace =', my_linspace(1, 7))

#%% Oppg 8.8

# a)

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 1

dx = 0.1

x_array = np.arange(-2, 2+dx, dx)
n = len(x_array)
y_array = np.zeros(n)

for i in range(0, n, 1):
    y_array[i] = f(x_array[i])

plt.close('all')
plt.plot(x_array, y_array, label='y')
plt.legend()
plt.xlabel('x')
plt.grid()

# plt.savefig('plot_fun_2ord.pdf')
plt.show()

    






















