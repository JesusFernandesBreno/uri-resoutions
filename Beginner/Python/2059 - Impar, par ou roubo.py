ns = str(input()).split()
ns = [int(i) for i in ns]

if ns[0] == 1:
    if (ns[1]+ns[2]) % 2 == 0:
        if ns[3] == 0 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
    else:
        if ns[3] == 0 and ns[4] == 0:
            print('Jogador 2 ganha!')
        elif ns[3] == 1 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
else:
    if (ns[1]+ns[2]) % 2 == 0:
        if ns[3] == 0 and ns[4] == 0:
            print('Jogador 2 ganha!')
        elif ns[3] == 1 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
    else:
        if ns[3] == 0 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 0:
            print('Jogador 1 ganha!')
        elif ns[3] == 1 and ns[4] == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
