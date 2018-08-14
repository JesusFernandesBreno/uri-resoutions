n = int(input())
tg = [0, 0]
for i in range(n):
    b = int(input())
    t = [[int(j) for j in str(input()).split()], [int(j) for j in str(input()).split()]]
    for c, j in enumerate(t):
        if j[2] % 2 == 0:
            tg[c] = j[0] + j[1] + b
        else:
            tg[c] = j[0] + j[1]

    if tg[0] > tg[1]:
        print('Dabriel')
    elif tg[0] < tg[1]:
        print('Guarte')
    else:
        print('Empate')

