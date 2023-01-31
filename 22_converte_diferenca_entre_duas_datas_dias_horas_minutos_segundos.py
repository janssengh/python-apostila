#converte_diferenca_entre_duas_datas_dias_horas_minutos_segundos

from datetime import datetime, time

def dif_em_segundos(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

def segundos_para_dhms(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    dias, horas = divmod(horas, 24)
    return(dias, horas, minutos, segundos)

#Data especificada
data1 = datetime.strptime('2022-01-30 21:37:00', '%Y-%m-%d %H:%M:%S')

#Data atual
data2 = datetime.now()

print("\n%d dias, %d horas, %d minutos, %d segundos" % segundos_para_dhms(dif_em_segundos(data2, data1)))





