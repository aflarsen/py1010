# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:43:25 2025

@author: AFL015

Oppg. kap. 7

"""

#%% Oppg 7.1

temp = float(input('Skriv inn temperatur: '))

if (temp <= 0):
    print('Vannet er frossent')
elif (temp < 100.00):
    print('Vannet er flytende')
else:
    print('Vannet koker')
    
#%% Oppg 7.2

siffer9 = int(input('Skriv inn midtsifferet i fnr ditt: '))

if siffer9 % 2 == 0:    # Wtf? Hvorfor kan man droppe parantesene??
    print('Du er hunnkjønn')
else:
    print('Du er hannkjønn')
    
#%% Oppg 7.3

# Se https://no.wikipedia.org/wiki/Kvadrant

x, y = map(int, input('Skriv inn tallverdier for x og y, adskilt med mellomrom: ').split())     # Litt mer komplisert enn nødvendig, kunne tatt inn hver for seg

if x > 0 and y > 0:
    print('P ligger i 1. kvadrant')
elif x > 0 and y < 0:
    print('P ligger i 4. kvadrant')
elif x < 0 and y > 0:
    print('P ligger i 2. kvadrant')
else:
    print('P ligger i 3. kvadrant')
    
#%% Oppg 7.4

minfart = int(input('Skriv inn din fart i km/h: '))

# Overtredelse o
o = minfart - 60
bot = 0

if o <= 0:
    print('Du kjører innenfor fartsgrensen.')
elif o <= 5:
    bot = 800
elif o <=10:
    bot = 2100
elif o <= 15:
    bot = 3800
elif o <= 20:
    bot = 5500
elif o <= 25:
    bot = 8500
else:
    print('Du mister lappen.')
    
print('Du får kr', bot, 'i bot.')

#%% Oppg 7.5

time = input('Skriv inn klokkeslett: ').split(':')  # denne løsningen gjør .split() unødvendig, bedre i oppg. 7.6

if time[0] >= '12' and time[0] <= '24':
    print("PM")
else:
    print("AM")
    
#%% Oppg 7.6

# Modifisert iht. løsning for oppg. 7.5

time = input("Skriv inn tid: ")

[hour, mins] = time.split(':')

hour = int(hour)
mins = int(mins)

if hour >= 12:
    print("It's", hour-12, ":", mins, "PM now.")
else:
    print("It's", hour, ":", "AM now.")
    
#%% Oppg 7.7

import numpy as np

arr1 = np.array([1, 2, 3, -5, 7, 0.1, -6]) #sum: 2.1

if_slo_til = 0

if arr1[2] > np.sum(arr1):
    if_slo_til += 1 # jepp
    print("test 1, jepp")

if np.size(arr1) == 6 and arr1[0] + arr1[3] < 0:
    if_slo_til += 1 # nope
    print("test 2, jepp")

if np.size(arr1) == 6 or arr1[0] + arr1[3] < 0:
    if_slo_til += 1 # jepp
    print("test 3, jepp")

if arr1[1]*arr1[2] >= 2 and arr1[-1] < 0 or arr1[0]**2 == 4:
    if_slo_til += 1 # nope (feil!)
    print("test 4, jepp", arr1[-1])
    
if  7 in arr1 and np.min(arr1) == -5:    
     if_slo_til += 1 # nope
     print("test 5, jepp")

print("Antall ganger if-testen slo til var", if_slo_til)

# Mitt svar: if-test slår inn 2x (feil!)

#%% Oppg 7.8

import numpy as np
import matplotlib.pyplot as plt

# Definer x-verdier
x = np.linspace(0, 2 * np.pi, 1000)  # Verdier fra 0 til 2*pi

# Beregn y-verdier
y = np.sin(x)

# Lag plottet
plt.plot(x, y, label='f(x) = sin(x)')
plt.title('Sinusfunksjonen')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Tegn x-aksen
plt.axhline(1, color='red', linewidth=0.5, linestyle='--', label='y = 1')  # y=1
plt.axhline(-1, color='blue', linewidth=0.5, linestyle='--', label='y = -1')  # y=-1
plt.legend()
plt.grid()
plt.show()

###

def f(x):
    return np.sin(x)

x_koor = float(input("Skriv inn en x-koordinat: "))

if x_koor < 0 or x_koor > 4*np.pi:
    print("x-koordinaten ligger utenfor intervallet")
else:
    if x_koor <= 0.5:
        print("f(x) er mindre eller lik 0,5")
    else:
        print("f(x) er større enn 0,5")






















