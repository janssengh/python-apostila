def dados_comuns(lista1,lista2):
    
    for x in lista1:
        for y in lista2:
            if x==y:
                return True
    return False      

print(dados_comuns([1,2,3,4,5],[5,6,7,8,9]))
print(dados_comuns([1,2,3,4,5],[6,7,8,9]))
