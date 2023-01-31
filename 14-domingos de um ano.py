from datetime import date, timedelta

def domingos(ano):
    # 1 de janeiro do ano
    data = date(ano,1,1)

    #primeiro domingo do ano
    data+=timedelta(days=6-data.weekday())

    while data.year == ano:
        #retorna a data sem destruir o estado variável
        yield data
        #avança 7 dias no ano
        data+=timedelta(days=7)

for d in domingos(2022):
    print(d)



