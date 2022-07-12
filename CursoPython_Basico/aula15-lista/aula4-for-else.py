"""
for / else
"""

variavel = ['fernando', 'Augusto', 'alves', 'batista']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('a'):
        # O comando .startswith() pergutna se a variável começa com a letra perguntada.
        # o comando .lower() converte as letras da variável para minuscula.
        print('Esta variável começa com A')
    else:
        print('Esta não começa com J')

