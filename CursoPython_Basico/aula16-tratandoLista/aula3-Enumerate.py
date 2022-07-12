"""
Split - divide uma string #str
Join - juntar uma lista #str
Enumerate - enumerar elementos da lista # interáveis.
"""
string = 'O Brasil é penta'
lista = string.split(' ')

for v1, v2 in enumerate(lista):  # V1 = indice - V2 = valor
    print(v1, v2)
print()
print(lista[3])