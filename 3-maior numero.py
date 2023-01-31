def maior_numero(lista):
    maior = lista[0]
    for x in lista:
        if x > maior:        
            maior = x
    return maior

lista1=[1,2,4,6]
lista2=[3,6,2]

print(maior_numero(lista1))
print(maior_numero(lista2))
