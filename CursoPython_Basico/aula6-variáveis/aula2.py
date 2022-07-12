nome = 'Fernando'
idade = 31
altura = 1.75
peso = 64.0
AnoAtual = 2022
imc = peso / altura ** 2
DataNascimento = AnoAtual - idade

print(f'{nome}, nascido em {DataNascimento}, possui {idade} anos, {peso} kg e imc de {imc:.1f}')