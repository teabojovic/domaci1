import math
"""
Napisati kod koji za dati pozitivni realni broj r računa i štampa obim i površinu kruga
poluprečnika r
"""
r = int(input("Unesite poluprečnik: "))
O = 2 * r * math.pi
P = r * r * math.pi
print(O, P)