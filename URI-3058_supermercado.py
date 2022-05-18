casos = int(input())
precos = []

for i in range(casos):
    valores = input().split()
    preco_carne = float(valores[0])
    gramas = int(valores[1])

    total = (1000 / gramas) * preco_carne
    precos.append(total)

print(f'{min(precos) :.2f}')