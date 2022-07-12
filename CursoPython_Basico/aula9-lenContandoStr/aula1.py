"""
Contar quantidade de caracteres de um usário
"""
usuario = input('Digite seu usuário: ')  # lembrando que tudo digitado numa input é lido como str
qtd_caracteres = len(usuario)  # conta os caracteres do usuario e os converte de str para int
# a função len só funciona para str, ela não funciona para números int ou float
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Usuário deve ter pelo menos 8 caracteres')
else:
    print('cadastrado no sitema')

