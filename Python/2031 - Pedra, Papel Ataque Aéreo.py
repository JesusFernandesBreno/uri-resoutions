n = int(input())
c = 0

while True:
    p = [input(), input()]
    if (p[0] == 'ataque' and p[1] == 'pedra') or (p[0] == 'pedra' and p[1] == 'ataque'):
        print('Jogador {} venceu'.format(p.index('ataque')+1))
    elif (p[0] == 'pedra' and p[1] == 'papel') or (p[0] == 'papel' and p[1] == 'pedra'):
        print('Jogador {} venceu'.format(p.index('pedra')+1))
    elif (p[0] == 'ataque' and p[1] == 'papel') or (p[0] == 'papel' and p[1] == 'ataque'):
        print('Jogador {} venceu'.format(p.index('ataque')+1))
    elif (p[0] == 'papel' and p[1] == 'papel'):
        print('Ambos venceram')
    elif (p[0] == 'pedra' and p[1] == 'pedra'):
        print('Sem ganhador')
    elif (p[0] == 'ataque' and p[1] == 'ataque'):
        print('Aniquilacao mutua')

    c += 1
    if c == n:
        break

