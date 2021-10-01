"""
Dva automobila se kreću po kružnoj stazi dužine L u suprotnim smjerovima. Polaze iz iste
tačke i kreću se stalnim brzinama v1 i v2. Na kom rastojanju će se naći automobili u
trenutku T. Ulaz: U jednom redu zadaju se 4 cijela broja L, v1, v2, T, razdvojeni blankom
(1 ≤ L, v1, v2, T ≤ 100). Izlaz: Štampati jedan cio broj – rastojanje automobila u trenutku T.
"""
L, v1, v2, T = map(int, input().split())
predjeni_put_1 = v1 * T
predjeni_put_2 = v2 * T
ukupno = predjeni_put_1 + predjeni_put_2
print(ukupno)
if ukupno > L:
    ukupno = ukupno % L
print(L - ukupno)