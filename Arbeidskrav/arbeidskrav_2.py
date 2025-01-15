# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:01:42 2025

Arbeidskrav 2, py1010

@author: Aleksander Larsen
"""

#%% 

# Oppg. 1

import datetime as dt

alder = int(input('Hvilket år er du født? '))

print('Du ble', 2024 - alder, 'i 2024.')
print('I år blir du', dt.datetime.now().year - alder, 'år.')

#%%

# Oppg. 2

import math as m

antall_elever = int(input('Skriv inn antall elever: '))

antall_pizzaer = int(m.ceil(antall_elever / 4))  # hint 2 virker unødvendig? kommer ut som heltall uansett, eller?

print('Det må kjøpes', antall_pizzaer, 'pizzaer.')

#%%

# Oppg. 3

import numpy as np

v_grad = float(input('Skriv inn gradtallet: ' ))

def fun_rad(g):
    return g*np.pi/180

print('Radianen er: ', fun_rad(v_grad))

#%%

# Oppg. 4

# a )

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# b)

land_inn = input('Skriv inn et land: ').capitalize()
by = data.get(land_inn)[0]
innb = data.get(land_inn)[1]
print(by,'er hovedstaden i', land_inn, 'og det er', innb, 'mill. innbyggere i', by)


# c)

nLand_inn = input('\nSkriv inn et nytt land: ').capitalize()
nBy = input('Skriv inn hovedstaden: ').capitalize()
nInnb = float(input('Skriv inn innbyggertallet: '))

data.update({nLand_inn: [nBy, nInnb]})

print('Dictionaryen er oppdatert:', data)


#%%

# Oppg. 5

a = float(input('Skriv inn grunnlinje: '))
b = float(input('Skriv inn høyde: '))

def fun_fig(a, b):
    areal_hsirkel = (np.pi*a**2)/2
    areal_rv3kant = (a*b)/2
    areal_fig = areal_hsirkel + areal_rv3kant
    
    omkr_hsirkel = 2*(np.pi*a)
    hypotenus = (a**2)+(b**2)
    omkr_fig = b+hypotenus+omkr_hsirkel
    
    return np.round([areal_fig, omkr_fig], decimals=2)

print('Figurens areal og omkrets er hhv:', fun_fig(a, b)[0], 'og', fun_fig(a, b)[1])

#%%

# Oppg. 6

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2-5

plt.plot(x, y)




