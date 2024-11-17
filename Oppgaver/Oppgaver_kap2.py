# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:08:57 2024

@author: AFL015

Oppgaver kap. 2

"""

#%% 

# 2.1

L = 100000

r = 23.4

R1 = 100000 * 0.234 / 12

print("Direkte utregning: ", R1)

R2 = L * (r/100) / 12

print("Utregning med variabler: ", R2)

#%%

# 2.2

F = 0

C = (F - 32) / 1.8

print(F, "grader Fahrenheit tilsvarer ", C, "grader Celsius.")

#%%

# 2.3

# pip list
# -> pygame vises ikke i listen
# pip install pygame
# pip list
# pygame vises i listen

#%%

# 2.4 a)

# time-funksjonen viser antall sekunder siden epoch (January 1, 1970, 00:00:00 (UTC)) som en float-verdi
# sleep-funksjonen setter utførelsen av en tråd på vent med det angitte antallet sekunder

# 2.4 b)

import time

delay = input("Skriv inn ønsket forsinkelse i sekunder: ")
start = time.time()
print("Du ønsket", delay, "sekunder forsinkelse. Starttid:", start,". -Sees etterpå!")
print("Zzzz...")
time.sleep(int(delay))
slutt = time.time()
print("Hei igjen, sluttiden er", slutt,".", "Dette bør ikke ha tatt særlig mer enn", delay, "sekunder.")
print("Fasit: sluttid - starttid =", slutt-start, "sekunder")


#%%

#