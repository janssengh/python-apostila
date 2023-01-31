def multiplicar_lista(itens):
    total=1
    for x in itens:
        total*=x
    return total

lista1=[1,2,4,6]
lista2=[3,6,2]

print(multiplicar_lista(lista1))
print(multiplicar_lista(lista2))
