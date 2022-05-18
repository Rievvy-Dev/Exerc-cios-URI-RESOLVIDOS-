while True:
    try:
        expressao = input()
        quantidade = []
    except EOFError:
        break
    for simbolos in expressao:
        if simbolos == '(':
            quantidade.append('(')
        elif simbolos == ')':
            if len(quantidade) > 0:
                quantidade.pop()
            else:
                quantidade.append(')')

    if len(quantidade) == 0:
        print('correct')
    else:
        print('incorrect')