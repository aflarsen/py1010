# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:54:57 2024

Arbeidskrav 1, py1010

@author: Aleksander Larsen

"""

# import numpy as np

print("\nBeregn årlig kostnad ved kjøp av elbil".upper(), "vs.", "bensinbil \n".upper())

# Antall kjørte km/år
xkm_aar = input("Skriv inn antall kilometer pr. år: ")
km_aar = float(xkm_aar)
# Forsikring
forsikring_el = 5000
forsikring_bensin = 7500
# Trafikkforsikringsavgift pr dag
trafikkavgift_aar = 8.38*365
# Drivstoffbruk
forbruk_el = 2*(0.2*km_aar)
forbruk_bensin = km_aar
# Bomavgift
bomavg_el = 0.1*km_aar
bomavg_bensin = 0.3*km_aar
# Totalkostnad
aarl_kost_el = sum([forsikring_el, trafikkavgift_aar, forbruk_el, bomavg_el])
aarl_kost_bensin = sum([forsikring_bensin, trafikkavgift_aar, forbruk_bensin, bomavg_bensin])

billigst = "bensinbil" if  aarl_kost_bensin < aarl_kost_el else "elbil"
dyrest = "bensinbil" if  aarl_kost_bensin > aarl_kost_el else "elbil"
aarl_diff = (aarl_kost_bensin - aarl_kost_el) if aarl_kost_bensin > aarl_kost_el else (aarl_kost_el - aarl_kost_bensin)

print("\nÅrlig kostnad elbil: NOK", f"{aarl_kost_el:.2f}", "\nÅrlig kostnad bensinbil: NOK", f"{aarl_kost_bensin:.2f}\n")
print("\u0332".join("Resultat:").upper())
print(billigst.capitalize(), "er billigst! \nDen årlige kostnadsdifferansen mellom", 
      billigst, "og", dyrest,"er NOK", "\u0332".join("\u0332".join(f" {aarl_diff:.2f}")), ".")