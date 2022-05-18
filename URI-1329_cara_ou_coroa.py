while 1:
    quantidade = int(input())
    
    if quantidade == 0:
        break
    
    resultados =  list(map(int, input().split()))
    
    mary = 0
    john = 0
    
    for i in resultados:
        if(i == 0):
            mary = mary + 1
        else:
            john = john + 1
    print('Mary won {} times and John won {} times' .format(mary, john))