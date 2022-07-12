secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print(f'Você perdeu!')
        break  # finaliza o código.

    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhhh... isso não vale, digite apenas uma letra')
        continue   # retorna o codigo para a função anterior (no caso o input)

    digitadas.append(letra)  # append insere na variável digitadas, a letra escreita.

    if letra in secreto:
        print('uhull, a letra faz parte da palavra secreta!')
    else:
        print(f'Afff: a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()  # apaga das digitadas, a letra escrita.

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(secreto_temporario)

    if secreto_temporario == secreto:
        print('PARABÉNS, VOCÊ GANHOU!')
        break  # finaliza o código.
    else:
        print(f'A palavra secreta era: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print()
