"""
mexendo com índices através de interação (ato de percorrer cada elemento da str) usando wile e if
"""


frase = 'O rato roeu a roupa do rei de roma'
tamanho = len(frase)
print(tamanho)
print(frase[5])

nova_str = ''
contador = 0
"""
while contador < tamanho:
    # print(frase[contador], contador)  # vai enumerar cada str em órdem.
    nova_str += frase[contador]  # ele vai pegar a str frase e vai jogando letra por letra, na str nova_str
    contador += 1
    print(nova_str)

print()
print(nova_str)
"""

# como alterar uma letra de mínuscolo para maíusculo em uma frase.
usuario = input('Qual letra você quer que fique maíuscula: ')

while contador < tamanho:
    letra = frase[contador]
    if letra == usuario:
        nova_str += usuario.upper()  # .upper() deixa a letra escolhida maíuscula.
    else:
        nova_str += letra
    contador +=1

print(nova_str)



