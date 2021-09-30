"""
Dato je rastojanje u centimetrima. Odrediti koliko cijelih metara ima u tom rastojanju.
Npr. 324cm imaju 3 metra.
"""

rastojanje_u_cm = int(input('Unesite rastojanje u centimetrima: '))

rastojanje_u_metrima = rastojanje_u_cm // 100
print ('Rastojanje u metrima iznosi', rastojanje_u_metrima, 'm')
