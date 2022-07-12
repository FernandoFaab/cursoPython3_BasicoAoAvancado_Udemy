lista1 = [0,1,2,3,4,5,6,7,8,9]

soma = 0
for valor in lista1:
    soma = soma + valor
print(soma)

lista2 = ['string', True, 10, -20.5]
for elem in lista2:  # elem diz que tipo de elemento tem cada valor da lista.
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}')
