#gera_calendario_HTML_dados_um_ano_mes_especifico

#o código gerado deverá ser inserido em um arquivo.html e ser aberto no navegador web

import calendar
htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
print(htmlcal.formatmonth(2023,1))

