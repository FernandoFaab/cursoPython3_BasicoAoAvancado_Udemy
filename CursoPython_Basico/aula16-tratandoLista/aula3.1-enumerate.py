lista = [
   #  0        1       2
    ['edu', 'joão', 'luiz'],  # 0
    ['maria', 'aline', 'joana'],  # 1
    ['helena', 'eduardo', 'luana'],  #2
]

for v1, v2 in enumerate(lista):
    print(v1, v2)

# print(lista[1][1])  # primeiro cochete será indice, segundo cochete será coluna.
print()

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome2)