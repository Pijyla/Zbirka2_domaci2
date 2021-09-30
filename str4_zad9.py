"""
Napisati kod koji za date stranice a, b i c kvadra računa i štampa površinu i zapreminu kvadra.
"""

stranica_a_kvadra = int(input('Stranica a kvadra iznosi '))
stranica_b_kvadra = int(input('Stranica b kvadra iznosi '))
stranica_c_kvadra = int(input('Stranica c kvadra iznosi '))

povrsina_kvadra = 2 * ((stranica_a_kvadra * stranica_b_kvadra) + (stranica_a_kvadra * stranica_c_kvadra) + (stranica_b_kvadra * stranica_c_kvadra))
print('Povrsina kvadra iznosi ', povrsina_kvadra)

zapremina_kvadra = stranica_a_kvadra * stranica_b_kvadra * stranica_c_kvadra
print('Zapremina kvadra iznosi ', zapremina_kvadra)

