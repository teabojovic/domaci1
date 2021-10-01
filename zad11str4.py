"""
Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće izrezati iz
tog pravougaonika?
"""
def broj_mogucih_kvadrata(a,b):
    k = 543 // 65
    p = 130 // 65
    return k * p
print( broj_mogucih_kvadrata(543,130))  