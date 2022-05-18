while True:
    try:
        quantidade_grupo = int(input())
        velocidade_lesmas = input().split()
        var_velocidade = 0
        
        for i in range(quantidade_grupo):
            if int(velocidade_lesmas[i]) > var_velocidade:
                var_velocidade = int(velocidade_lesmas[i])
                
        if var_velocidade < 10:
            nivel = 1
        elif var_velocidade >= 10 and var_velocidade < 20:
            nivel = 2
        else:
            nivel = 3
            
        print(nivel)
        
    except EOFError:
        break