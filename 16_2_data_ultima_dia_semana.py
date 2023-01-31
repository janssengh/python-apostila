import turtle


#entradanum = turtle.numinput("Último dia da semana informada", "Núm.dia da semana")

entradanome = turtle.textinput("Último dia da semana informada", "Nome dia da semana")
#print (entradanum)
print (entradanome)


diasemana=['segunda','terça','quarta','quinta','sexta','sábado','domingo']
        
print(list(enumerate(diasemana)))

for i,x in enumerate(diasemana):
    if x == entradanome:
        indice = i
        
print(indice)


from datetime import date
from datetime import timedelta

hoje=date.today()

diferenca=(hoje.weekday()-indice)%7

ultimo_dia_semana=hoje-timedelta(days=diferenca)

print(ultimo_dia_semana)




