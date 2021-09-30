"""
Date su 3 kovanice: galeoni, srpovi i knutovi, pri čemu se zna da 1 galeon vrijedi 17 srpova, a 1 srp vrijedi 29 knutova.
Potrebno je napraviti program koji za zadatu količinu galeona, srpova i knutova štampa kolika je ukupna količina tog novca u knutovima.
ULAZ: U jedinom redu ulaza nalaze se, odvojena razmakom, tri prirodna broja G, S i K (0 <= G, S, K <= 50).
IZLAZ: U jedini red izlaza štampa se prirodan broj koji predstavlja trazenu kolicinu novca.
"""


galeoni, srpovi, knutovi = input('Unesite vrijednosti galeona, srpova i knutova: ').split()
galeoni = int(galeoni)
srpovi = int(srpovi)
knutovi = int(knutovi)

kolicina_knutova = (((galeoni * 17) + srpovi) * 29) + knutovi
print (kolicina_knutova)



