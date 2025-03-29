"""
Loesningsforslag til arbeidskrav 1 i PY1010 2024-2025

Finn Aakre Haugen (finn.haugen@usn.no)

Oppdatert 2024 11 09

"""


#%% Kjoerelengde
# Tegnsekvensen #%% ovenfor markerer begynnelsen på en kodecelle.

kjoerelengde = 10000  # [km/aar]

# Alternativt bruke input-funksjonen for aa lese inn fra konsollen:
# kjorelengde = int(input('Angi kjoerelengde [km/aar]: '))

#%% Forsikring

forsikring_E = 5000  # [kr/aar]
forsikring_B = 7500  # [kr/aar]

#%% Trafikkforsikringsavgift

antall_dager_per_aar = 365
trafikkforsikringsavgift_per_dag_E = 8.38  # [kr/d]
trafikkforsikringsavgift_per_dag_B = 8.38  # [kr/d]
trafikkforsikr_E = (
    trafikkforsikringsavgift_per_dag_E * antall_dager_per_aar)  # [kr]
trafikkforsikr_B = (
    trafikkforsikringsavgift_per_dag_B * antall_dager_per_aar)  # [kr]

#%% Drivstoff
    
drivstofforbruk_E = 0.2  # [kWh/km]
drivstoffpris_E = 2  # [kr/kWh]
drivstoffkost_E = drivstofforbruk_E * drivstoffpris_E

drivstoffkost_B = 1.0  # [kr/km]

#%% Bompenger

bom_E = 0.1  # [kr/km]
bom_B = 0.3  # [kr/km]

#%% Totale kostnader

total_kost_E = (forsikring_E 
                   + trafikkforsikr_E
                   + drivstoffkost_E * kjoerelengde
                   + bom_E * kjoerelengde)

total_kost_B = (forsikring_B 
                   + trafikkforsikr_B
                   + drivstoffkost_B * kjoerelengde
                   + bom_B * kjoerelengde)

kostdiff = total_kost_B - total_kost_E

# I print-funksjonene nedenfor er det benyttet såkalt
# f-streng-formattering (f-string formatting) for å sette antall sifre
# etter desimalskilletegnet.

print(f'Total aalig kostnad elbil [kr] = {total_kost_E:.0f}')
print(f'Total aarlig kostnad bensinbil [kr] = {total_kost_B:.0f}')
print(f'Aarlig kostnadsdiff (bensinbil - elbil) [kr] = {kostdiff:.0f}')

# Utskrift uten f-streng-formatering (Python velger da antall sifre):
# print('Total aalig kostnad elbil [kr] =', total_kost_E)
# print('Total aarlig kostnad bensinbil [kr] =', total_kost_B)
# print('Aarlig kostnadsdiff (bensinbil - elbil) [kr] =' , kostdiff)

