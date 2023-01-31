def menor_numero(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:        
            menor = x
    return menor

lista1=[1,2,4,6]
lista2=[3,6,2]

print(menor_numero(lista1))
print(menor_numero(lista2))
