#imprime_calendario_ano_todo

import calendar
cal= calendar.TextCalendar(calendar.SUNDAY)

#ano:2022,largura da coluna:2, linhas por semana:1
#número de espaços entre colunas do mês: 1
#3: número de meses por coluna
print(cal.formatyear(2023,2,1,1,3))
