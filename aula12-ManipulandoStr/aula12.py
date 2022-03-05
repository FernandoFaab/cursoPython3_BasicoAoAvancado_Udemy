"""
Manipulando strings
* string indices - fatiamento de strings [inicio:fim:passo] - função built-in len, abs, type, print e etc.
"""
# positivos [012345678] - os números (começando no 0) de cada lebra da string abaixo, isso é um indice.
texto =     'Python s2'
print(texto[2])
print(texto[8])

# para você tirar um caractere da string é só colocar [:- o numero dos caracteres que quer retirar]
print(texto[:-1])  # não vai imprimir o 2 da str.
# você também pode fatiar uma string.
testando_a_string_anteriro = texto[2:6]  # se você não escreve o primeiro numero, ele começará do zero.
# se você começa com o número e depois coloca :, ele vai começar do número que tu escreveu.
print(testando_a_string_anteriro)  # vai imprimir só o thon - da str texto.
print(texto[3:])  # vai imprimir hon s2
print(texto[:3])  # vai imprimir pyt

testando_a_string_pulando = texto[0::2]  # ele vai pular letras de 2/2
print(testando_a_string_pulando)  # vai imprimir PTO 2