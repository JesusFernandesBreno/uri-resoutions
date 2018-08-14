caso = 0
while True:
    try:
        caso += 1
        n1 = input()
        n2 = input()
        sub = 0
        pos = 0
        for i in range(0,len(n2)):
            if n1 == n2[i:len(n1)+i]:
                sub += 1
                pos = i+1
        if sub == 0:
            print('Caso #{}:'.format(caso))
            print('Nao existe subsequencia\n')
        else:
            print('Caso #{}:'.format(caso))
            print('Qtd.Subsequencias: {}'.format(sub))
            print('Pos: {}\n'.format(pos))
    except EOFError:
        break
