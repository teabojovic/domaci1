"""
 (*) Domino se igra pločicama pravougaonog oblika, takvim da se na svakoj pločici nalaze
dvije oznake. Svaka oznaka sastoji se od određenog broja tačkica. Broj tačkica zavisi o
veličini skupa domina. U skupu domina veličine N broj tačkica na jednoj pločici može biti
bilo koji broj između 0 i N, uključivo. U jednom skupu ne postoje dvije pločice potpuno
jednakih oznaka, bez obzira na redosljed oznaka na pločici. U potpunom skupu veličine N
nalaze se sve moguće pločice sa oznakama 0 do N. Npr. potpuni skup domina veličine 2
sadrži šest pločica sa sljedećim oznakama:
Napišite program koji će odrediti ukupan broj tačkica na svim pločicama u potpunom
skupu domina veličine N. Vaš program treba da učita jedan prirodan broj N (1 ≤ N ≤ 1000)
– veličinu potpunog skupa domina. Program treba da štampa ukupan broj tačkica na svim
pločicama u potpunom skupu domina veličine N. 
"""
"""
Sa jedne strane imamo: 
ZA DOMINU 1 ( domina sa jednom tackicom) - spaja se sa dominom 0 i dominom 1
ZA DOMINU 2 - spaja se sa dominom 0, dominom 1 i dominom 2
...
A sa druge strane imamo:
ZA DOMINU 1 - dominu 0 ( koju smo vec uracunali u prethodni zbir), dominu 1
ZA DOMINU 2 - dominu 0 (vec uracunata), domina 2 i domina 1
...
Ukupno se saberu ove dvije sume
"""

N = int(input("Unesite broj N: "))
i = 1
suma = 0
prva_strana = 0
while i <= N:
    suma = i * (i + 1) 
    prva_strana = prva_strana + suma 
    i = i + 1
# suma gdje je npr. kod domine 1 jedna tackica fiksirana i pojavljuje se 2 puta (sa nulom i jedinicom)
# pa se kod domine 2 fiksira strana sa dvije tackice i ona se pojavljuje tri puta (sa 0, 1, 2)...
# druga_strana =  1 + (1 + 2) + (1 + 2 + 3)... + (1 +...+ N) jer je na prvoj strani broj tackica fiksiran,
# a na drugoj strani se on mijenja
i = 1
k = 1
suma = 0
suma_sume = 0
while i <= N:
    while k <= i:
        suma = k/2 * (1 + k)
        k = k + 1
    suma_sume = suma_sume + suma
    i = i + 1
    k = 1
ukupno = prva_strana + suma_sume
print(ukupno)

  