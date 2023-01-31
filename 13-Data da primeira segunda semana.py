import time

#ano semana dia_da_semana
#0 = domingo
#1 = segunda
print(time.asctime(time.strptime('2022 19 1','%Y %W %w')))
