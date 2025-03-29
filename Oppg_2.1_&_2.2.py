# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:14:33 2024

@author: Aleksander


Oppg 2.1

"""

L = 100000

r = 23.4

R1 = 100000 * 0.234 / 12

print("Direkte utregning: ", R1)

R2 = L * (r/100) / 12

print("Utregning med variabler: ", R2)


"""
Oppg 2.2

"""

F = 0

C = (F - 32) / 1.8

print(F, "grader Fahrenheit tilsvarer ", C, "grader Celsius.")

#%% Skriver ut streng: 
print("hello world")

#%%
print("Kalle")

#%% Bruker-input i console:
x = input("Skriv inn et tall: ")

#%% Strengformatering:
print("Dette er verdien av grader Celsius, formatert til 2 desimaler etter komma: ", f"C = {C:.2f}")