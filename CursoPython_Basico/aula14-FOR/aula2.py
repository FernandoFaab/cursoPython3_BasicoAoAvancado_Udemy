"""
Mudando uma letra na str para maíuscula usando .upper() e o for
"""
texto = 'python'
nova_str = ''
for letra in texto:
    if letra == 't':
        nova_str += letra.upper()
    else:
        nova_str += letra
print(nova_str)

# lembrando que se você usar BREAK, quando chega naquela str ele vai parar o laço.
# lembrando que se voçê usar o CONTINUE, ele vai pular aquela parte do laço, que você colocou.
