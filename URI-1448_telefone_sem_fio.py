from sys import stdin
stdin.reconfigure(encoding='latin-1')

casos = int(input())

pontos_totais = 0

for i in range(casos):
    frase_correta = input()
    pontos_time1 = 0
    pontos_time2 = 0
    primeiro_acertou = 0
    frase_time1 = input()
    frase_time2 = input()
    tamanho = len(frase_correta)
    
    for letra in range(tamanho):
        if frase_correta[letra] == frase_time1[letra]:
            pontos_time1 = pontos_time1 + 1
            if primeiro_acertou == 0 and frase_time2[letra] != frase_correta[letra]:
                primeiro_acertou = 1
        if frase_correta[letra] == frase_time2[letra]:
            pontos_time2 = pontos_time2 + 1
            if primeiro_acertou == 0 and frase_time1[letra] != frase_correta[letra]:
                primeiro_acertou = 2
        
        pontos_totais = pontos_totais + 1
    
    print('Instancia {}' .format(i + 1))
    
    if pontos_time1 > pontos_time2:
        print('time 1')
    elif pontos_time2 > pontos_time1:
        print('time 2')
    else:
        if pontos_time1 == pontos_totais and pontos_time2 == pontos_totais or (pontos_time1 == 0 and  pontos_time2 == 0) or primeiro_acertou == 0:
            print('empate')
        elif pontos_time1 == pontos_time2 and primeiro_acertou == 1:
            print('time 1')
        elif pontos_time1 == pontos_time2 and primeiro_acertou == 2:
            print('time 2')
    print()