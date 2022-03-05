"""
For in - em python
interando str com for
função range(start=0, stop, step=1) você diz onde quer que comece o range, deposi onde para, e de quanto em quanto pula.
"""

texto = 'Python'
for letra in texto:  # exibirá cada letra, mas com um código mais simples, do que se fosse usado while. (sem contador)
    print(letra)

print()

for n in range(0,10,2):  # se eu coloco só um número, esse numero será o stop e o zero do start será padrão.
    print(n)

print()
# o start não pode ser menor que o stop, a menos que você for fazer uma regressiva. Ai o step tem que ser -1
for x in range(20, 10, -1):
    print(x)

print()

for y in range(80):
    if y % 8 == 0:  # aqui você esta procurando os multiplos de 8 no range de 0 até 80
        print(y)
