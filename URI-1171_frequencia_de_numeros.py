quantidade = int(input())
lista = {}
for i in range(quantidade):
    var = int(input())
    if(var in lista):
        lista[var] += 1
    else:
        lista[var] = 1

chaves = lista.keys()
chaves = sorted(chaves)

for i in chaves:
    print('{} aparece {} vez(es)' .format(i, lista[i]))