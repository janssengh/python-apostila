import datetime

hoje=datetime.date.today()
ontem=hoje-datetime.timedelta(days=1)
amanha=hoje+datetime.timedelta(days=1)

print('Ontem:',ontem)
print('Hoje:',hoje)
print('Amanhã:',amanha)


        
