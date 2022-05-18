from math import pow
casos = int(input())

for i in range(casos):
    numero = input().split()
    
    c = int(numero[0])
    d = int(numero[1])
    
    if c == 0 and d == 0:
        print('0')
    else:
        calculo_consoantes = int(pow(26, c))
        calculo_digitos = int(pow(10, d))

        placa = calculo_consoantes * calculo_digitos

        print(placa)