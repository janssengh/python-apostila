#            0         1        2       3       4       5
cores = ['Vermelho','Verde','Branco','Preto','Rosa','Amarelo']

print([x for(i,x) in enumerate(cores) if i not in (0,4,5)])

#Explicando enumerate:
#retorna um objeto composto por tuplas:(indice,valor)

#converte objeto enumerate em lista e imprime todas as tuplas
print(list(enumerate(cores)))

#percorre o objeto enumerate usando for
for i,x in enumerate(cores):
    print(i,x)
