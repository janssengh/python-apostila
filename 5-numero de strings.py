#Exemplo de lista:['abc','xyz','aba','1221']
#Resultado:2

def verifica_palavras(lista):
    contador=0

    for palavra in lista:
        if len(palavra)>=2 and palavra[0]==palavra[-1]:
            contador+=1
    return contador

lista1=['abc','xyz','aba','1221']
lista2=['osso','casa','gato','1234']

print(verifica_palavras(lista1))
print(verifica_palavras(lista2))
