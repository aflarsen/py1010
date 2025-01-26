# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:17:26 2025

@author: Aleksander Larsen

Oppg. kap. 5

"""
#%% Oppg 5.1

# Funksjonen ser ut til å regne ut arealet til en rettvinklet trekant. 

#%% Oppg 5.2

def fun_rektangel(g, h):
    A = g*h
    return A

print('Areal =', fun_rektangel(4.5, 4))

#%% Oppg 5.3

def fun_valuta(e):
    NOK = e*10.42
    USD = e*1.19
    return [NOK, USD]

euro = float(input('Skriv inn antall Euro: '))

print('€ in NOK:', round(fun_valuta(euro)[0],2), '\n€ in USD:', round(fun_valuta(euro)[1], 2))

# Løsning iht boken, samme men litt annerledes:
    
def fun_valuta(e):
    NOK = e*10.42
    USD = e*1.19
    return NOK, USD

NOK, USD = fun_valuta(euro)

print('€ in NOK:', NOK, '\n€ in USD:', USD)

#%% Oppg 5.4

import numpy as np

def fun_storekatet(lk, hy):
    sk =  np.sqrt(hy**2-lk**2)
    # sk2 = sk = hy**2-lk**2   -uten bruk av numpy eller matlab
    # sk = sk2**0.5
    return sk

a = float(input('Skriv inn kateten: '))
c = float(input('Skriv inn hypotenusen: '))

print(np.round(fun_storekatet(a, c), 2)) # OBS: hypotenusen må være større enn kateten, ellers blir tallet negativt som gir feil. Evt må man ha en sjekk på hvilket input-tall som er størst feks

#%% Oppg 5.5

# Fungerer denne, hva skrives i så fall ut?

x = 10

def myfun ():
    print ( x )

myfun ()

# Mitt svar: Ja, det fungerer. Skriver ut 10

#%% Oppg 5.6

# Fungerer denne? Hva skrives evt ut?

x = 10

def myfun ():
    # x = x + 1  # gir feil
    print ( x )

myfun ()

# Mitt svar: Ja, det fungerer. Skriver ut 11
# Løsning: feil! UnboundLocalError: cannot access local variable 'x' where it is not associated with a value. Skulle feks vært x =+ 1

#%% Oppg 5.9

Ep = 34.37
m = 0.48
g = 1.6

def fun_hoydeOverBakken(Ep, m, g=9.81):
    h = Ep/(m*g)
    return h

print(fun_hoydeOverBakken(Ep, m, g))

#%% Oppg 5.10

import numpy as np
import matplotlib.pyplot as plt

def fun_f(x):
    return x**2+3

def fun_g(x):
    return 3*x-1

xa = np.linspace(-2, 3, 100)

plt.close('all')
plt.figure(1, figsize=(12, 9))
plt.plot(xa, fun_f(xa), xa, fun_g(xa))
plt.legend(labels=('fun_f(x)', 'fun_g(x)'))
# plt.savefig('plot_fun_plot.pdf')
plt.show()

#%% Tester moduler før oppg 5.16..

import sys
#sys.path.append('C:/Users/AFL015/USN_py_gk/py1010/Oppgaver/moduler') # absolutt sti
sys.path.append('moduler')  # relativ sti
import minmodul as mm

#import importlib
#importlib.reload(mm)

mm.greeting("Jonathan")

x = dir(mm)
print('Innhold i minmodul.py:', x)

#%% Oppg 5.16
import sys
sys.path.append('moduler')
import rektangel_modul as rm

L = 3.0
B = 4.0 

print('Areal rektangel:', rm.areal_rektangel(L, B))
print('Omkrets rektangel:', rm.omkrets_rektangel(L, B))
print('Diagonal rektangel:', rm.diagonal_rektangel(L, B))


















