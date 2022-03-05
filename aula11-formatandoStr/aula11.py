"""
Como formatar valores com modificadores
:s - testo (str)      :d - inteiro (int)      :f - nuúmeros flutuantes real (float)
:.(numero)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
> - esquerda       < - direita        ^ - centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))  # formatando as casas decimais.
print(f'{divisao:.3f}')  # jeito mais simples de formatar casas decimais.
print()  # pula uma linha

num3 = 1
print(f'{num3:0>3}')  # coloca numeros determinados a esquerda da variável(lembrando que o número conta como caractere)
print(f'{num3:0<3}')  # coloca numeros a determinados direita da variável(lembrando que o número conta como caractere)
print(f'{num3:0^5}')  # coloca a variável no centro de números determinados(lembrando que o número conta como caractere)

nome = 'fernando'
sobrenome = 'augusto'
print('{}{}{}'.format(nome, ' ', sobrenome))
print(nome, sobrenome)
print(nome.lower())  # minusculo
print(nome.upper())  # maiusculo
print(nome.title())  # primeira letra maiuscula