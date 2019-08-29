n =  int(input())

tot = 0
tot_c = 0
tot_r = 0
tot_s = 0

for i in range(n):
    cobaia = str(input()).split()
    tot += int(cobaia[0])

    if cobaia[1] == 'C':
        tot_c += int(cobaia[0])
    elif  cobaia[1] == 'R':
        tot_r += int(cobaia[0])
    elif cobaia[1] == 'S':
        tot_s += int(cobaia[0])

print('Total: {} cobaias'.format(tot))
print('Total de coelhos: {}'.format(tot_c))
print('Total de ratos: {}'.format(tot_r))
print('Total de sapos: {}'.format(tot_s))
print('Percentual de coelhos: {:.2f} %'.format((tot_c * 100) / tot ))
print('Percentual de ratos: {:.2f} %'.format((tot_r * 100) / tot))
print('Percentual de sapos: {:.2f} %'.format((tot_s * 100) / tot))
