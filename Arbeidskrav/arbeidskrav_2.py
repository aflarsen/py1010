# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:01:42 2025

Arbeidskrav s, py1010

@author: AFL015
"""

#%% 

# Oppg. 1

import datetime as dt

alder = int(input('Hvilket år er du født? '))

print('Du ble', 2024 - alder, 'i 2024.')
print('I år blir du', dt.datetime.now().year - alder, 'år.')

#%%

# Oppg. 2

antall_elever = int(input('Skriv inn antall elever: '))

