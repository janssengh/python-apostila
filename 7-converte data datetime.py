from datetime import date
from datetime import datetime

data=date.today()
print(data)#somente data
print(datetime.combine(data, datetime.min.time()))# data e hora
        
