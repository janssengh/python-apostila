#data_hora_sistema_GMT_local

from time import gmtime, strftime
import time

ano=2023
mes=2 #fevereiro
#          0         1       2        3        4       5        6
dias = ['segunda','terça','quarta','quinta','sexta','sábado','domingo']

# GMT (Tempo médio)
#      GMT:                  Mon, 30Jan202311:59:22 PM Hora oficial do Brasil
print('GMT:' + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
#      Local:              Mon,30Jan2023 08:59:22 PM Hora oficial do Brasil
print('Local:' + strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))
#              Mon, 30 Jan 2023 09:09:19
print(strftime("%a, %d %b %Y %I:%M:%S\n"))
#             PM, Hora oficial do Brasil
print(strftime("%p, %Z\n"))





