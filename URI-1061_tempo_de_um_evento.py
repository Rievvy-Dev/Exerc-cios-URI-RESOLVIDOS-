dia_inicial = input ().split()
inicio_evento = input ().split()
dia_final = input ().split()
final_evento = input().split()

dia_i = int(dia_inicial[1])
dia_f = int(dia_final[1])
hora_inicial = int(inicio_evento[0])
minuto_inicial = int(inicio_evento[2])
segundo_inicial = int(inicio_evento[4])
hora_final = int(final_evento[0])
minuto_final = int(final_evento[2])
segundo_final = int(final_evento[4])

dias = dia_f - dia_i
horas = hora_final - hora_inicial
minutos = minuto_final - minuto_inicial
segundos = segundo_final - segundo_inicial

if segundos < 0:
    segundos = segundos + 60
    minutos = minutos - 1
if minutos < 0:
    minutos = minutos + 60
    horas = horas - 1
if horas < 0:
    horas = horas + 24
    dias = dias - 1
    
print(dias, 'dia(s)')
print(horas, 'hora(s)')
print(minutos, 'minuto(s)')
print(segundos, 'segundo(s)')