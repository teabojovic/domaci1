"""
Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre
"""
trocifreni_broj = int(input('Unesite trocifren broj '))

cifra_stotina = trocifreni_broj // 100
cifra_desetica = (trocifreni_broj // 10) % 10
cifra_jedinica = trocifreni_broj % 10

cifra_stotina_kopija = cifra_stotina

cifra_stotina = cifra_jedinica
cifra_jedinica = cifra_stotina_kopija

novi_trocifreni_broj = (cifra_stotina * 100) + (cifra_desetica * 10) + cifra_jedinica
print(novi_trocifreni_broj)