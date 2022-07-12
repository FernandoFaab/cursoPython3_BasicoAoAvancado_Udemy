"""
Operadores Lógicos  - and, or, not - in, not in
"""
# Usando and, as duas precisam ser verdadeiras.
# True E True = True # True E False = Flase # False E False = False
comparacao1 and comparacao2

# usando OR/OU, apenas uma precisa ser verdadeira.
# True E true = True  # True E False = True  # False E False = False
comparacao1 or comparacao2

# not inverte a pergunta da expressão, ou o valor da expressão.
a = 2
b = 3
if not b > a:
    print('B é maior que A')
else:
    print('A é maior que B')
# vai ser impresso else, porque a pergunta do if foi: se a nãoi foir maior que b, imprima else. Graças ao not!

# O in, serve para perguntar se algo existe na variável. not in, perguntaria se não existe.
nome = 'fernando'
if 'cad' in nome:
    print('existe')
else:
    print('não existe')  # a resposta será não existe.

if 'fer' not in nome:
    print('Não existe')  # a resposta será existe.
else:
    print('existe')