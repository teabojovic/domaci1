import math
"""
Napisati kod koji za dati poluprečnik osnove r i visinu H prave kupe računa površinu i
zapreminu kupe. 
"""
r = int(input("Unesi poluprečnik osnove: "))
H = int(input("Unesi visinu kupe: "))
s = math.sqrt(r * r + H * H)
P = r * math.pi * (r + s)
V = 1/3 * r *r * math.pi * H
print( P, V)
