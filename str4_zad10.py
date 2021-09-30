"""
Napisati kod koji za dati poluprečnik osnove r i visinu H prave kupe računa površinu i zapreminu kupe.
"""


poluprecnik_kupe_r = int(input('Poluprecnik r kupe iznosi '))

import math

#Izvodnica kupe
s = 2 * poluprecnik_kupe_r

#Visina kupe
h = math.sqrt(s**2 - poluprecnik_kupe_r**2)
print(h)

povrsina_kupe = poluprecnik_kupe_r * 3.14 * (poluprecnik_kupe_r + s)
print('Povrsina kupe iznosi ', povrsina_kupe)

zapremina_kupe = ((poluprecnik_kupe_r**2 * 3.14) / 3) * h
print('Zapremina kupe iznosi ', zapremina_kupe)

