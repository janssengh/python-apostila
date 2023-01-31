#primeiro_dia_semana_numero_dias_mes_ano

from calendar import monthrange

ano=2023
mes=2 #fevereiro
#          0         1       2        3        4       5        6
dias = ['segunda','terça','quarta','quinta','sexta','sábado','domingo']

tupla = monthrange(ano, mes) #(2,28) - 2(quarta),28(ultimo dia do mes)

print(tupla)
print(dias[tupla[0]], 'é o primeio dia do mês')




