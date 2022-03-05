nome = input('Escreva o seu primeiro nome de usuário: ')
caracteres = len(nome)

if caracteres <= 4:
    print('Seu nome é curto')
elif caracteres <= 6:
    print('Seu nome é normal')
else:
    print('seu nome é muito grande')
