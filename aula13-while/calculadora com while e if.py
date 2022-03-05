"""
Calculadora
"""
while True:
    num1 = input('Digite um número: ')
    operador = input('digite um operador: ')
    num2 = input('Digite outro número: ')


    if not num1.isnumeric() or not num2.isnumeric():
        # .isnumeroc() Se a cadeia contém apenas caracteres numéricos, ele retorna True, caso contrário False
        print('Você precisa digitar um número!')
        continue  # continue fará com que nenhum operador abaixo seja digitado. (no caso de não digitar número)

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('erro')
        sair = input('Deseja sair? [s] sim ou [n] não: ')
        if sair == 's':
            break


