import datetime

hoje = datetime.datetime.now()
dia_do_ano = (hoje-datetime.datetime(hoje.year,1,1)).days+1

print(dia_do_ano)


    

        
