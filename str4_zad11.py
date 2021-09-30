"""
Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće izrezati iz tog pravougaonika?
"""

sirina_pravougaonika = 543
visina_pravougaonika = 130

stranica_kvadrata = 65

kvadrata_po_visini_pravougaonika = 130 // 65

kvadata_po_sirini_pravougaonika = (543 // 65) * kvadrata_po_visini_pravougaonika
print('Moguce je izrezati ', kvadata_po_sirini_pravougaonika, 'kvadrata.')
