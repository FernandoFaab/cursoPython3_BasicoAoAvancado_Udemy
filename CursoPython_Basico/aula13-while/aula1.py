"""
while - enquanto uma condição for verdadeira
"""
nome = 0
while nome != 'fernando':  # enquanto nome escrito não for fernando, vai gerar um loop, pedindo para digitar o nome.
    nome = input('Qual o seu nome? ')
    print(f'ola {nome}!')

x = 0
while x < 5:  # vai contar números de 0 até a condição.
    print(x)
    x = x + 1
print()

# agora vamos fazer um while dentro de outro while

coluna = 0
while coluna < 5:
    linha = 0
    while linha < 5:
        print(f'coluna = {coluna} e linha = {linha}')
        linha += 1  # isso quer dizer que linha sera igual a linha + 1
    coluna += 1
print('fim')