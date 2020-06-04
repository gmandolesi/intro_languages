## Function date_time.py
# Objectives:
#   1. Date
#   2. Time
#
# Input: None
# Output: None
#
# How to run this code:
#       python date_time.py

from datetime import date, time, datetime, timedelta

## DATE
hoje = date.today()
print(hoje)  # yyyy-mm-dd

# several date manipulation are possible. consult documentation.
print(hoje.strftime('%d/%m/%y')) #dd/mm/yy


## TIME
horario = time(hour = 15, minute= 18, second=36)
horario_str = horario.strftime('%H:%M:%S')


##DATETIME
data_completa = datetime.now()
data_atual = data_completa.strftime('%d-%m-%Y')
horario_atual = data_completa.strftime('%H:%M:%S')
data = data_completa.strftime('%c')
dia = data_completa.weekday()

tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom')
print(tupla[dia])


data_proposta = '01/10/2020'
data_proposta = datetime.strptime(data_proposta, '%d/%m/%Y')

nova_data = data_proposta + timedelta (days = 7)