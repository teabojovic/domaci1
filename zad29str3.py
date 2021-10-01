"""
Data su tri cijela broja A, B, C. Odrediti da li među njima ima bar jedan paran broj i bar
jedan neparan broj. Ulaz: Prvi red ulaza sadrži tri cijela broja A, B i C (1 ≤ A ≤ 1000). Izlaz:
Štampati „YES“ ili „NO“. 

"""
A, B, C = map(int, input().split())
paran = 0
neparan = 0
if A % 2 == 0:
    paran = 1
else:
    neparan = 1
if B % 2 == 0:
    paran = paran + 1
else:
    neparan = neparan + 1
if C % 2 == 0:
    parean = paran + 1
else:
    neparan = neparan + 1
if paran > 0 and neparan > 0:
    print("YES")
else:
    print("NO")