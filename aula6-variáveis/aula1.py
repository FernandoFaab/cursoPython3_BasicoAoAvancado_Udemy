nome = 'Luiz Otávio'
idade = 32
altura = 1.80
MaiorIdade = idade > 18
peso = 80
imc = peso/ altura ** 2

print(nome, 'tem', idade, 'e seu imc é:', imc)

print(f'{nome} tem {idade} e seu imc é: {imc:.2f}')
"""
"f string" (f'') serve para simplificar o uso da string, 
fazendo com que você não precise mais colocar várias aspas e virgulas, para imprimir funções. 
dentro de uma f'string você pode simplificar números reais muito grande. Colocando :.2f
"""
print('{} tem {} e seu imc é: {:.2f}'. format(nome, idade, imc))
"""
A função desta forma acima, é outra maneira de se usar para imprimir. Mas, lembre-se de colocar
as variáveis na ordem dos cochetes e a formatação dos números após a virgula, 
tem que ficar dentro do cochete onde quer que seja formatado, não ao lado do nome da variável.
"""