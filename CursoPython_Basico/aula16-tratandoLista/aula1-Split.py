"""
Split - divide uma string #str
Join - juntar uma lista #str
Enumerate - enumerar elementos da lista # interáveis.
"""
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista = string.split(' ')  # divide uma str, no local do caractere especificado.
lista2 = string.split(',')
print(lista)
print(lista2)

for valor in lista:
#    print(lista.count(valor))  # conta quantas vezes a palavra apareceu na lista.
    print(f'A palavra "{valor}" apareceu {lista.count(valor)} x na frase.')  # conta quantas vezes a palavra apareceu.

print()
# código para contar qual palavra apareceu mais vezes (no caso ele vai reconhecer a última em caso de empate)

palavra = ''
contagem = 0
for valor in lista:
    quantidade = lista.count(valor)
    if quantidade > contagem:
        contagem = quantidade
        palavra = valor
print(f'A palavra que mais apareceu é "{palavra}" ({contagem}x)')

print()

for valor in lista2:
    print(valor.strip().capitalize())
# strip() retira o espaço do inicio da frase capitalize() coloca a primeira letra em maíusculo
