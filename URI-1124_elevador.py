from math import sqrt, pow


while True:
    saida = False
    tamanhos = input().split()
    largura = int(tamanhos[0])
    comprimento = int(tamanhos[1])
    raio1 = int(tamanhos[2])
    raio2 = int(tamanhos[3])
    
    if largura == 0 and comprimento == 0 and raio1 == 0 and raio2 == 0:
        break

    if raio1 > raio2:
        maior = raio1 + raio1
    else:
        maior = raio2 + raio2
    
    if maior <= largura and maior <= comprimento:
         if (sqrt(pow((largura  - raio2  - raio1), 2) + pow((comprimento  - raio2  - raio1), 2))  >=  raio1  + raio2):
            saida = True 

    if saida == True:
        print('S')
    else:
        print('N')