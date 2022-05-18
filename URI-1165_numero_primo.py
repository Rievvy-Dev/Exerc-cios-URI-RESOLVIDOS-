casos = int(input())

for i in range(casos):
    numero = int(input())
    
    primo = True
    for j in range(2, numero):
        if numero % j == 0:
            primo = False
            break
        
    if primo:
        print('{} eh primo' .format(numero))
    else:
        print('{} nao eh primo' .format(numero))