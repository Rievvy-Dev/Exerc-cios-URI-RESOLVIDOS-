while True:
    try:
        senha = input()
        tamanho_senha = len(senha)
        maiuscula = False
        minuscula = False
        numero = False
        
        if tamanho_senha > 32 or tamanho_senha < 6:
            print('Senha invalida.')
        else:
            for i in range(tamanho_senha):
                if(ord(senha[i]) > 64 and ord(senha[i]) < 91):
                    maiuscula = True
                elif(ord(senha[i]) > 96 and ord(senha[i]) < 123):
                    minuscula = True
                elif(ord(senha[i]) > 47 and ord(senha[i]) < 58):
                    numero = True
                else:
                    maiuscula = False
                    break
            if(maiuscula and minuscula and numero):
                print('Senha valida.')
            else:
                print('Senha invalida.')
    
    except EOFError:
        break