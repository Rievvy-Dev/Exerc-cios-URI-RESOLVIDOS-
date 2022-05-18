from decimal import Decimal
valor = input()
if Decimal(valor) >= 0 and valor[0] != '-':
    print('+', end='')
    
print('%.4E' % Decimal(valor))