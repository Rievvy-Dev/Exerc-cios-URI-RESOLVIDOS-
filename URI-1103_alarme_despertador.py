while True:
    try:
        tempo = input().split()
        if tempo[0] == '0' and tempo[1] == '0' and tempo[2] == '0' and tempo[3] == '0':
            break
    except EOFError:
        break
        
    hora_inicial = int(tempo[0])
    minuto_inicial = int(tempo[1])
    hora_final = int(tempo[2])
    minuto_final = int(tempo[3])
    
    horas_dormidas = hora_final - hora_inicial
    if horas_dormidas < 0:
        horas_dormidas += 24
    if hora_inicial == hora_final and minuto_final < minuto_inicial:
        horas_dormidas = 24   
    minutos_dormidos =  minuto_final - minuto_inicial
    horas_em_minutos = horas_dormidas*60
    minutos = minutos_dormidos + horas_em_minutos

    print(minutos)