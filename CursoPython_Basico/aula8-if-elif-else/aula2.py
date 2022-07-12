"""
Operadores relacionais + if elif else
"""
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
# Lembrando que tem que converter o input em int, porque input sempre lê no formato str
IdadeMinima = 18
IdadeMaxima = 60


if idade >= IdadeMinima and idade <= IdadeMaxima:
    print(f'{nome}, pode pegar o empréstimo.')
else:
    print(f'{nome}, fora do limete de idade.')
