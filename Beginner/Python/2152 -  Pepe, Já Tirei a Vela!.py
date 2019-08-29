n = int(input())
for i in range(n):
    hrs = str(input()).split()
    if len(hrs[0]) == 1:
        hrs[0] = '0'+hrs[0]
    if len(hrs[1]) == 1:
        hrs[1] = '0'+hrs[1]
    if hrs[2] == '1':
        print('{}:{} - A porta abriu!'.format(hrs[0],hrs[1]))
    else:
        print('{}:{} - A porta fechou!'.format(hrs[0],hrs[1]))
