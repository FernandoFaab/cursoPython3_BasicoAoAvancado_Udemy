"""
Entrada de dados
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade: ')

print(f'O usuário digitou: {nome}, e o tipo da variável é: {type(nome)}')

"""
impout é o que faz o programa ler e armazenar. A função, sempre fica gravada no formato str, mesmo se for número. 
então não daria para fazer contas, mas você pode converter a str em ingeiro. 
#  colocar o tipo de fuhnção que quer converter e a variável entre parenteses, converte a variável.
"""
AnoDeNascimento = int(idade) - 2022
print(f'{nome} tem {idade} anos')


