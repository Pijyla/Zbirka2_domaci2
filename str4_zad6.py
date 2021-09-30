"""
Za neku drzavu poznata je njena povrsina i broj stanovnika. Odrediti gustinu naseljenosti te drzave.
"""

broj_stanovnika = int(input('Unesite broj stanovnika '))
povrsina_drzave = int(input('Unesite povrsinu drzave '))

gustina_naseljenosti_drzave = broj_stanovnika / povrsina_drzave
print(round(gustina_naseljenosti_drzave))
