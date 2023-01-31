def soma_lista(itens):
    soma=0
    for x in itens:
        soma+=x
    return soma

lista1=[1,2,-8]
lista2=[0,-5,18,1,7,10]

print(soma_lista(lista1))
print(soma_lista(lista2))
