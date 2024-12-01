# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:45:35 2024

@author: AFL015

Oppgaver kap. 3

"""

# 3.1 Beløp med renter, formatert

belop = 10000

rente = 1.85

res_5aar = belop*(1+rente/100)**5

print("Resultat 5 år:", f"{res_5aar:.2f}")

#%%

# 3.2 Tak og gulv

# ceil runder opp
# floor runder ned
# NB: numpy returnerer float-, math returnerer int-verdi
# np.ceil() kan ta imot  en hel liste/array og runde alle tallene samtidig. Math.ceil() kan bare ta imot ett tall om gangen. 

import numpy as np
import math as m

c = m.ceil(2.1)
f = m.floor(2.9)

print(c)
print(f)

c = np.ceil(2.1)
f= np.floor(2.9)

print(c)
print(f)

#%%

# 3.3 Avstand mellom to punkter

import numpy as np

xA = 2.3
yA = 8.1
xB = 7.4
yB = -13.5

avstand = np.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Avstanden mellom pkt A og B er:", f"{avstand:.3e}")

#%%

# 3.4 Samme som over, men som input

import numpy as np

xA = float(input("Skriv inn xA = "))
yA = float(input("SKriv inn yA = "))
xB = float(input("Skriv inn xB = "))
yB = float(input("Skriv inn yB = "))

avstand = np.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Avstanden mellom pkt A og B er:", f"{avstand:.3e}")

#%%

# 3.5 Kule

import numpy as np

radius = float(input("Skriv inn radius: "))

overflate = 4*np.pi*radius**2
volum = (4*np.pi*radius**3)/3 

print("Overflaten til kulen:", f"{overflate:.2f}", "\nVolumet til kulen:", f"{volum:.2f}")

#%%

# 3.6 Trekant

import numpy as np

lille_katet = float(input("Skriv inn lille katet: "))
hypotenus = float(input("Skriv inn hypotenusen: "))

store_katet = np.sqrt(hypotenus**2 - lille_katet**2)
print("Store katet er:", store_katet)

omkrets = lille_katet + hypotenus + store_katet
print("Omkretsen er:", omkrets)

areal = (lille_katet*store_katet)/2
print("Arealet til trekanten er:", areal)

#%%

# 3.7 Vinkler i trekant

import numpy as np

lilleK = float(input('Lengden av lille katet = '))
hypo = float(input('Lengden av hypotenusen = '))

storeK = np.sqrt(hypo**2 - lilleK**2)

v1 = np.arctan(lilleK/storeK)
v2 = np.arctan(storeK/lilleK)
v3 = np.pi/2
print('Kontroll: Sum av vinkler skal vÃ¦re 180:',
      np.degrees(v1 + v2 + v3)) 

print('Vinklene i rad er:',
      f'{v1:.4f},',
      f'{v2:.4f},',
      f'{v3:.4f}')
print('Vinklene er grader er:',
      f'{np.degrees(v1):.1f},',
      f'{np.degrees(v2):.1f},',
      f'{np.degrees(v3):.1f}')

#%%

# 3.8 Tuppel

odd = (1, 3, 5, 7, 9, 11, 13)
primes = (3, 5, 7, 11, 13)

mix = odd + primes

print('11 occur', mix.count(11), 'times in mix')
print('14 in mix is', 14 in mix)

#%%

# 3.9 Dictionary

pannekaker = {"hvetemel" : "3dl", "salt" : "0.5ts", "egg" : 4, "melk" : "6dl", "smør" : "2ss"}

print(pannekaker)
print("Lengde på dictionary:", len(pannekaker))
print("Type of collection:", type(pannekaker))
print("List of key:value pairs in dictionary:", pannekaker.items())
print("List of keys in dictionary:", pannekaker.keys())
print("List of values in dictionary:", pannekaker.values())

# loop:
for x in pannekaker:
    print(x, ":", pannekaker[x])

#%%

# 3.10 Liste

navn = ['Wald', 'Anne', 'Tor', 'Mari']
print(navn[2] + navn[0].lower(), "og", navn[3] + navn[1].lower())

#%%

# 3.11 Teskststreng

setning = 'Hanne og Stine er snille'
sListe = setning.split()
print(sListe)
sListe.reverse()
print(sListe)
print(sListe[0].upper(), sListe[1:5]) # måtte ha concatinert alle for at det skulle vært helt riktig, men..

#%%

# 3.12 Liste med navn og nummer

navn = ['Eli', 'Ola', 'Ali', 'Ela'] 
tlf = [9423234, 9223001, 4756001, 9592676]

print('Velg og skriv inn et av følgende navn:')
person_valgt = str(input(navn[0:]))
posisjon = navn.index(person_valgt.capitalize())
print('Nr til den valgte personen er:', tlf[posisjon])

#%%

# 3.13 Fra tekst til liste til integer

s = 'Nedre grense for karakter E er 40 poeng.'
sListe = s.split()
print(sListe)
i = int(sListe.index('40'))
print('Variabelen "i" er nå av typen', type(i))

#%%

# 3.14

















