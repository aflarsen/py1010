# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 11:25:00 2025

@author: Aleksander Larsen

Prosjektoppgave "Support dashboard"

"""

#%% Del A

import pandas as pd

xldata = pd.read_excel('support_uke_24.xlsx')  # Spyder krever visst den absolutte stien selv om den ligger i samme mappe som py-filen, mens Jp notebook er happy med bare filnavnet

u_dag = xldata['Ukedag'].values
kl_slett = xldata['Klokkeslett'].values
varighet = xldata['Varighet'].values
score = xldata['Tilfredshet'].values

#%% Del B

import matplotlib.pyplot as plt

days = {}

# legger inn dagene fra u_dag i dictionary
for i in u_dag:
    days[i] = 0

# summerer antall henvendelser pr dag
for i in u_dag:
    if(i == 'Mandag'):
        days[i] += 1
    elif(i == 'Tirsdag'):
        days[i] += 1
    elif(i == 'Onsdag'):
        days[i] += 1
    elif(i == 'Torsdag'):
        days[i] += 1
    elif(i == 'Fredag'):
        days[i] += 1

x = days.keys()
y = days.values()

plt.bar(x, y)
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.show()

#%% Del C

mx = max(varighet)
mn = min(varighet)

delstr = mn.split(":")  # bruker .split() bare for å ha prøvd det
sek = delstr[2]

print("Lengste samtale varte i", mx[3:5], "minutter og", mx[6:8], "sekunder.",  # bruker slice ("strings are arrays")
      "\nKorteste samtale varte i", sek, "sekunder.")

#%% Del D

import numpy as np
import time

# gjør om fra string til sekunder
def strToSecs(tidStr):
    toTime = time.strptime(tidStr, '%H:%M:%S')
    toSecs = toTime.tm_hour * 3600 + toTime.tm_min * 60 + toTime.tm_sec
    return toSecs

# tester strToSecs() 👌
assert strToSecs('03:22:11') == 12131, "feil i strToSecs()"

toSecsArr = np.array([])

# legger sekundverdier i ny array
for i in varighet:
    toSecsArr = np.append(toSecsArr, strToSecs(i))

# finner snitt i sekunder    
snInSecs = int(np.mean(toSecsArr))

# omformatterer snitt i sekunder til 'hh:mm:ss'
avgTime = time.strftime('%H:%M:%S', time.gmtime(snInSecs))

# skriver ut resultatet
print("Gjennomsnittlig samtaletid basert på alle henvendelser i uke 24 er", 
      int(avgTime[0:2]), "timer", int(avgTime[3:5]), "minutter og", int(avgTime[6:8]), "sekunder.")

#%% Del E

t8_10 = t10_12 = t12_14 = t14_16 = 0

# looper gjennom klokkeslettene og teller opp
for i in kl_slett:
    if(int(i[0:2]) >= 8 and int(i[0:2]) < 10):
        t8_10 += 1
    elif(int(i[0:2]) >= 10 and int(i[0:2]) < 12):
        t10_12 += 1
    elif(int(i[0:2]) >= 12 and int(i[0:2]) < 14):
        t12_14 += 1  
    elif(int(i[0:2]) >= 14 and int(i[0:2]) < 16):
        t14_16 += 1
    else:
        print("Noen har jobbet sent 🥱")
        
sizes = [t8_10, t10_12, t12_14, t14_16]
labels = ["8-10", "10-12", "12-14", "14-16"]
bang = (0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, explode=bang)
plt.legend(title = "Tidsrom")
plt.show()

#%% Del F

total = positive = passive = negative = 0 

# luker ut nans og fordeler på svargruppene
cleanScore = ([])

for i in score:
    if not np.isnan(i):
        if i >=1 and i <=6:
            negative += i
        elif i >= 9 and i <= 10:
            positive += i
        else:
            passive += i
        total += i
        cleanScore.append(i)

# net promotor score = % positive kunder - % negative kunder
nps = ((positive / total) * 100) - ((negative / total) * 100)
print("Net promotor score for MORSEs supportavdeling uke 24 er:", np.round(nps, 2)) 
        
plt.pie([positive, passive, negative], labels=["Positiv", "Passiv", "Negativ"], 
        autopct='%1.1f%%', startangle=90, shadow=True, explode=(0.05, 0.05, 0.05))
plt.legend(title="NPS")
plt.show()
        















