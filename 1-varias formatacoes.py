import time
import datetime

print("Data e hora atual: ",datetime.datetime.now())
print("Ano atual: ",datetime.date.today().strftime("%Y"))
print("Mês do Ano: ",datetime.date.today().strftime("%B"))
print("Número da semana no ano:",datetime.date.today().strftime("%W"))
print("Dia da semana na semana:",datetime.date.today().strftime("%w"))
print("Dia do ano:",datetime.date.today().strftime("%j"))
print("Dia do mês:",datetime.date.today().strftime("%d"))
print("Dia da semana:",datetime.date.today().strftime("%A"))
