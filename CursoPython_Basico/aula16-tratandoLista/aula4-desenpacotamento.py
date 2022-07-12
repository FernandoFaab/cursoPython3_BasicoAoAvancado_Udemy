"""
Desenpacotamento de lista
"""
lista = ['luiz', 'joão', 'maria']

n1, n2, n3 = lista  # torna cada valor da lista em uma variável.
print(n2)

n1, n2, *outra_lista = lista  # * cria outra lista, com os valores que não foram suados como variável.
# serve para descartar o resto de uma lista.
print(outra_lista)

*outra_lista, n2, n3 = lista  # colocando o *primeiro, ele seleciona os primeiros, e as variáveis viram os últimos.
print(n3)