l = [[str(input()).split() for j in range(2)] for i in range(int(input()))]
for i in l:
    for j in range(3):
        i[1][j] = int(i[1][j])
for c,i in enumerate(l):
    if i[0][0] == 'eye':
        print('Caso #{}: {}'.format(c+1,int((0.3*i[1][0]) + (0.59*i[1][1]) + (0.11*i[1][2]) ) ))
    elif i[0][0] == 'mean':
        print('Caso #{}: {}'.format(c+1,int((i[1][0]+i[1][1]+i[1][2])/3) ))
    elif i[0][0] == 'min':
        print('Caso #{}: {}'.format(c+1,sorted(i[1])[0]))
    elif i[0][0] == 'max':
        print('Caso #{}: {}'.format(c+1,sorted(i[1],reverse=True)[0]))
