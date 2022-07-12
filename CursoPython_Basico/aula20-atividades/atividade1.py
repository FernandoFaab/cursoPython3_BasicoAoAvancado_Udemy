"""
Imprima os números abaixo usando for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
# for é usado para quando tu sabe o fim, while é usado para quando não se sabe. Neste caso sabemos o fim, usamos for.

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
# no caso, aqui se gerou um contador regressivo, e antes do contador, se enumerou cada sentença do for.
# Ou seja, não se fez duas colunas rodando, se fez uma coluna regressiva, sendo enumerada.

print()
# este jeito achei mais coerente. Se cria um while e no print, coloca um número expecifico - a variável.
i = 0
while i >= 8:
    print(i, 9-i)
    i += 1

print()
# Melhor de todos, este realmente fez rodar duas colunas
n1 = 0
for n2 in range(10, 1, -1):
    print(f"{n1},{n2}")
    n1 += 1
