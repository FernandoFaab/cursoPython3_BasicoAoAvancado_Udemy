"""
Tipos de dados
str - string/textos 'assim' "assim"
int - inteiro
float - real (sempre usar ponto e não virgula, para separar casas decimais)
bool - boleano/lógico - true/false

para saber o tipo de uma função, você pode usar o comando print(type(função))
"""
print('luiz', type('luiz'))
print(10, type(10))
print(25.25, type(25.25))
print(10 == 10, type(10 == 10))

# dados vazios, string vazia ou zero, são considerados bool false.
print(bool(0))

print(type(int('10')))  # esta formula converte um typo de dado, para outro tipo
print(type(str(10)))  # esta formula converte um typo de dado, para outro tipo
print(int(10.0))

"""
ATIVIDADE
"""
# nome: str
print('Fernando', type('Fernando'))
# idade: int
print(30, type(30))
# altura: float
print(1.75, type(1.75))
# É maior de idade?: bool
print(30>18, type(30>18))






