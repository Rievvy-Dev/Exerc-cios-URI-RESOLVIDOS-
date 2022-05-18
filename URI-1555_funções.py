import math

casos = int(input())

for i in range(casos):
    coordenadas = input().split()
    ponto_x = int(coordenadas[0])
    ponto_y = int(coordenadas[1])

    funcao_rafael = pow((3*ponto_x),2) + pow(ponto_y, 2)
    funcao_beto = 2*(pow(ponto_x,2)) + pow((5*ponto_y), 2)
    funcao_carlos = -100*ponto_x + pow(ponto_y, 3) 
    
    if funcao_rafael > funcao_carlos and funcao_rafael > funcao_beto:
        print('Rafael ganhou')
    if funcao_beto > funcao_carlos and funcao_beto > funcao_rafael:
        print('Beto ganhou')
    if funcao_carlos > funcao_rafael and funcao_carlos > funcao_beto:
        print('Carlos ganhou')