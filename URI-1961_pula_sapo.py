def entrada():
    
    p,n = map(int,input().split())
    altura = input().split()
    
    for i in range(len(altura)):
        altura[i] = int(altura[i])
        
    return p,n,altura


def verifica(a,b,p):
    
    if abs(a-b) > p:
        return True
    else:
        return False

def main():
    
    p,n,altura = entrada()
    a = False
    
    for i in range(n-1):
        a = verifica(altura[i],altura[i+1],p)
        
        if a == True:
            print('GAME OVER')
            break
        
    if a == False:
        print('YOU WIN')
        
main()