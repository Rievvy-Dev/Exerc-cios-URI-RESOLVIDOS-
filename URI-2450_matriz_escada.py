def main():
    from sys import stdin, stdout

    def checar_matriz(linhas, colunas, matriz):
        index = -1
        tudo_zero = False
        for i in range(linhas):
            curr_index = -1
            for j, numero in enumerate(matriz[i]):
                if numero != 0:
                    if tudo_zero:
                        return False
                    curr_index = j
                    break
            if curr_index == -1:
                tudo_zero = True
            else:
                if curr_index <= index:
                    return False
                index = curr_index
        return True

    linhas, colunas = map(int, stdin.readline().split())
    matriz = [list(map(int, stdin.readline().split())) for _ in range(linhas)]
    stdout.write('S\n' if checar_matriz(linhas, colunas, matriz) else 'N\n')

main()