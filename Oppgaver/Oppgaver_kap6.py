# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:34:19 2025

@author: AFL015

Oppg kap 6

"""

#%% Oppg 6.1

# Test av programmet fra oppg 5.8:
    
def finnH(energi, m, g):
    #omformer ligning til h=E/(m*g)
    h = energi/(m*g)
    return h

masse = 0.48
gravitasjon = 9.81
potensiellE = 34.37

hoyde = finnH(potensiellE, masse, gravitasjon)

print("h [m] =", hoyde)

# Løsningssvar: Vi tester programmet ved  ̊a sammenlikne programmets resultat med beregning utført manuelt i f.eks. konsollen eller med kalkulator: 
# h = Ep / mg   =   34,37 / 0,48*9,81   =   7.29909955827387 
# Dette er det samme som programmet gir, hvilket tyder p ̊a at programmet fungerer som forventet.

#%% Oppg 6.2

v = float ( input ('Skriv inn din vekt her [ kg ]: '))
h = float ( input ('Skriv inn din hoyde her [ m ]: '))
bmi = v / (h * h)   # Feilen var at det manglet parantes her (evt kunne man også skrevet h**2). Sjekket med BMI-kalkulator på nett at det var riktig resultat nå
print ("Din BMI er" , bmi)

#%% Oppg 6.3

# Riktig program:
import numpy as np
import matplotlib.pyplot as plt

def f (x):
    return (x**2)/3

def dfdx (x):
    return 2* x/3

def tangent (x , punkt ):
    return dfdx (punkt) * (x - punkt) + f(punkt)

a = 1.0
xa = np.linspace (0 , 4 , 100)
plt.close ('all')
plt.plot (a , f(a) , 'ro' , label = ' f(a) ')
plt.plot (xa , f(xa) , label = 'f(xa)')
plt.plot (xa, tangent(xa, a), label = 'tangent')
plt.legend ()
plt.xlabel ('x')
plt.grid ()
# plt.savefig ( ' plot_elev1.pdf ')
plt.show ()

#%% Oppg 6.4

# for kjedelig, dropper denne :P

