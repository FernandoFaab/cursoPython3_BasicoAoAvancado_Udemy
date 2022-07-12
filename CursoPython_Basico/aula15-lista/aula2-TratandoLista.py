lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2  # faz uma função ser completada por outra.
print(lista3)
lista1.extend(lista2)  # essa função faz uma lista, ser completada por outra lista também, mas sem criar outra variável.
print(lista1)

lista1.extend('a')  # acrescenta um valor ao final da lista
print(lista1)
lista1.append('b')  # também acrescenta um valor ao final da lista
print(lista1)
lista1.insert(1, 'aqui')  # Insere um ítem na lista, onde você quizer.
print(lista1)
lista1.pop(0)  # elimina um ítem da lista, se você não colocar o valor, ele vai eliminar o último.
print(lista1)
del(lista1[3:5])  # exclui o intervalo selecionado da lista
print(lista1)
print(max(lista3))  # fala qual o maior valor da lista
print(min(lista3))  # fala qual o menor valor da lista

lista4 = list(range(1, 10))  # Você cria uma lista, usando a função range.
print(lista4)
print(lista4[3])