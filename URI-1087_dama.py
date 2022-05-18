while True:
    try:
        posicao = input().split()
        
        x1 = int(posicao[0])
        y1 = int(posicao[1])
        x2 = int(posicao[2])
        y2 = int(posicao[3])
        
        diagonalx = (x1 - x2)**2
        diagonaly = (y1 - y2)**2
        
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            break
        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2:
            print(1)
        elif diagonalx == diagonaly:
            print(1)
        else:
            print(2)
        
    except EOFError:
        break