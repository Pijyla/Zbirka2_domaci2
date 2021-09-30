"""
Date su stranice a i b pravougaonika. Naći njegov obim i površinu.
"""

stranica_a = int(input('Stranica a pravougaonika iznosi: '))
stranica_b = int(input('Stranica b pravougaonika iznosi: '))

povrsina_pravougaonika = stranica_a * stranica_b
print('Povrsina pravougaonika iznosi:', povrsina_pravougaonika)

obim_pravougaonika = (2 * stranica_a) + (2 * stranica_b)
print('Obim pravougaonika iznosi:', obim_pravougaonika)
