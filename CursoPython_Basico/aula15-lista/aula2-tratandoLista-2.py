lista = [1,2,3,4,5]

n1, n2, *n = lista
print(lista)  # aqui eu imprimi a lista inteira
print(n1,n2,n)  # aqui eu desempacotei 2 itens da lista, e deixei o resto na função *n empacotado.
print(*lista)  # aqui eu desempacotei toda a alista
print(*lista, sep=';')  # aqui eu separei a lista com ;