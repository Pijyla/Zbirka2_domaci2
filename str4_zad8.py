"""
Napisati kod koji za dati pozitivni realni broj r racuna i stampa obim i povrsinu kruga poluprecnika r.
"""

poluprecnik_kruga_r = int(input('Unesite vrijednost poluprecnika kruga r: '))

povrsina_kruga = (poluprecnik_kruga_r * poluprecnik_kruga_r) * 3.14
print ('Povrsina kruga iznosi ', povrsina_kruga)

obim_kruga = 2 * poluprecnik_kruga_r * 3.14
print('Obim kruga iznosi ', obim_kruga)
