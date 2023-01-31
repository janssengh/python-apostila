#calcula_idade_anos_partir_data

from datetime import date

def calcula_idade(data):
    hoje = date.today()
    return hoje.year - data.year - ((hoje.month, hoje.day)<(data.month, data.day))

print(calcula_idade(date(1822,9,7))) #independência do Brasil
print(calcula_idade(date(1969,7,20))) #ida à lua
