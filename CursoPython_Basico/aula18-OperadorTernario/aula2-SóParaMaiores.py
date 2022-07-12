"""
Operador ternário em Python
"""
idade = input('Digite sua idade: ')

"""
if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar')
"""
if not idade.isnumeric():
    print('você precisa digitar apenas números')
else:
    idade = int(idade)
    de_maior = (idade >= 18)
    mensagem = 'pode acessar' if de_maior else 'não pode acessar'
    print(mensagem)