#16_data_ultima_terca

from datetime import date
from datetime import timedelta

hoje=date.today()

diferenca=(hoje.weekday()-1)%7
ultima_terca=hoje-timedelta(days=diferenca)

print(ultima_terca)
