"""
exemplo usando and, usuário e senha, loguin em sistema.
"""

usuario = input('Digite o nome do usuário: ')
senha = input('Digite sua senha: ')

usuario1 = 'fernando'
senha1 = '123456'

if usuario1 == usuario and senha1 == senha:  # como usei and, os dois deveriam ser certos. Se fosse or apenas um teria.
    print('Loguin concluído com sucesso')
else:
    print("Usuário ou senha inválidos")