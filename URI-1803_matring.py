linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()
resultado = ''
x = len(linha1) - 1

coluna_inicial = int(linha1[0])*1000 + int(linha2[0])*100 + int(linha3[0])*10 + int(linha4[0])
coluna_final = int(linha1[x])*1000 + int(linha2[x])*100 + int(linha3[x])*10 + int(linha4[x])

for i in range(x):
    if i != 0:
        coluna_codigo = int(linha1[i])*1000 + int(linha2[i])*100 + int(linha3[i])*10 + int(linha4[i])

        calculo = (coluna_inicial*coluna_codigo + coluna_final)%257
        resultado += chr(calculo)

print(resultado)