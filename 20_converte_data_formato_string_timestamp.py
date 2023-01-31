#converte_data_formato_string_timestamp

import time
import datetime

data_string = '13/05/2022'

print(time.mktime(datetime.datetime.strptime(data_string, "%d/%m/%Y").timetuple()))



