def procura_palavras(str,comp):
    selecionadas = []
    lista = str.split(" ")
    for x in lista:
        if len(x)>comp:
            selecionadas.append(x)
    return selecionadas

print(procura_palavras("Laranjas são frutas, tomates são legumes, alface é verdura e é isso ai", 4))
