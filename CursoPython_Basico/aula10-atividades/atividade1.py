numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é impar')
else:
    print('isso não é um número inteiro')