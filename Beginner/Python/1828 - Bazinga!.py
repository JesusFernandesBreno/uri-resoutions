pos = ['papel', 'pedra', 'tesoura', 'lagarto', 'Spock']
n_testes = int(input())
c = 0
while True:
    l = str(input()).split()
    ln1 = pos.index(l[0])
    ln2 = pos.index(l[1])

    if ln1 == ln2:
        print('Caso #{}: De novo!'.format(c+1))
    elif ln1 == 2 and ln2 == 0:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 0 and ln2 == 1:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 1 and ln2 == 3:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 3 and ln2 == 4:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 4 and ln2 == 2:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 2 and ln2 == 3:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 3 and ln2 == 0:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 0 and ln2 == 4:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 4 and ln2 == 1:
        print('Caso #{}: Bazinga!'.format(c+1))
    elif ln1 == 1 and ln2 == 2:
        print('Caso #{}: Bazinga!'.format(c+1))
    else:
        print('Caso #{}: Raj trapaceou!'.format(c+1))
        
    c += 1
    if c == n_testes:
        break
    

