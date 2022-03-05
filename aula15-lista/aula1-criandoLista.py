"""
Listas em python - fatiamento - append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4
lista = ['a', 'b', 'c', 'd', 'e']  # fazendo assim, eu posso colocar o valor com qualquer tamanho, e vai sair no print.
#    -    5    4    3    2    1
print(lista[1])

# string = 'abcde'  # agora fazendo deste jeito, sempre vai aprecer somente uma letra, do indice escolhido.
# print(string[1])

lista[3] = 'casa'  # fazendo isso, eu mudo o que estava escrito na lista, na posição 3
print(lista[3])

print(lista[0:3])
# vai imprimir este intervalo na lista. Se você omitir o primeiro valor, ele será 0 naturalmente.
# agora se você colocar o priemiro número com : e depois nada, o fim será o fim da lista.
print(lista[::2])  # aqui ele vai pular a lista, de 2x2
print(lista[::-1])  # aqui fará a lista ficar ao contrário.
