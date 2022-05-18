casos = int(input())

for i in range(casos):
    numero = int(input())
    soma = 0
    for j in range(1, numero):
        if numero % j == 0:
            soma += j
    if soma == numero:
        print('{} eh perfeito' .format(numero))
    else:
        print('{} nao eh perfeito' .format(numero))