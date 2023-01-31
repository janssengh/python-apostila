#Método 1

lista = [(10,20,30,20,10,50,60,40,80,50,40)]
itens_unicos = []

for x in lista:
    if x not in itens_unicos:
        itens_unicos.append(x)

print(itens_unicos)
 


