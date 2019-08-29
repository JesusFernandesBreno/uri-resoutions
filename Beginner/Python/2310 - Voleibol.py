n = int(input())
c = 0
tot = [[0,0], [0,0], [0,0]]
while True:
    l = [str(input()).split() for i in range(3)]
    tot[0][0] += int(l[1][0])
    tot[0][1] += int(l[2][0])
    tot[1][0] += int(l[1][1])
    tot[1][1] += int(l[2][1])
    tot[2][0] += int(l[1][2])
    tot[2][1] += int(l[2][2])
    c += 1
    if c == n:
        break
print('Pontos de Saque: {:.2f} %.'.format((tot[0][1]*100)/tot[0][0]))
print('Pontos de Bloqueio: {:.2f} %.'.format((tot[1][1]*100)/tot[1][0]))
print('Pontos de Ataque: {:.2f} %.'.format((tot[2][1]*100)/tot[2][0]))
