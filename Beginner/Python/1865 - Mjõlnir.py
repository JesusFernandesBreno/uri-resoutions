t = int(input())
c = 0

while True:
    linha =  str(input()).split()


    if linha[0] == 'Thor':
        print('Y')
    else:
        print('N')

    c += 1
    if c == t:
        break
