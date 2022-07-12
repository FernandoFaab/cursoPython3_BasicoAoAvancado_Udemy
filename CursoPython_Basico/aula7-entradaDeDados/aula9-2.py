"""
fazer uma calculadora
"""
numero_1 = int(input('digite um número: '))  # O int antes do input é porque o input sempre é gravado com str
numero_2 = int(input('digite um número: '))
numero_2 = int(numero_2)  # Ou se pode converter a variável para que ela de str vire outro tipo, como int.
print('soma dos números: ', numero_1 + numero_2)
