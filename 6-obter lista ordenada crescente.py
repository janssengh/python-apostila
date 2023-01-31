#Exemplo: [(2,5),(1,2),(4,4),(2,3),(2,1)]
#Resultado: [(2,1),(1,2),(2,3),(4,4),(2,5)]

def ultimo(tupla):
    return tupla[-1]

def ordenar_pelo_ultimo(lista):
    return sorted(lista, key=ultimo)

lista = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print (ordenar_pelo_ultimo(lista))
 


