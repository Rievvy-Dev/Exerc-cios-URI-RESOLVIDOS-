while True:
    try:
        numeros = input().split()
        numero1 = int(numeros[0])
        numero2 = int(numeros[1])
        soma1 = 1
        soma2 = 1
        for i in range(1,numero1 + 1):
            soma1 = soma1 * i
        for i in range(1,numero2 + 1):
            soma2 = soma2 * i
        print(soma1 + soma2) 
    except EOFError:
        break