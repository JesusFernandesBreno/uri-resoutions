def ret():
    if (l[0]**2 + l[1]**2)**(1/2) == l[2] or (l[1]**2 + l[2]**2)**(1/2) == l[0] or (l[0]**2 + l[2]**2)**(1/2) == l[1]:
        print('S')
    else:
        print('N')
l = [int(i) for i in str(input()).split()]

if abs(l[1]-l[2]) < l[0] and l[0] < l[1] + l[2]:
    if l[0] == l[1] and l[1] == l[2]:
        print('Valido-Equilatero')
        print('Retangulo: ', end='')
        ret()
    elif l[0] == l[1] or l[1] == l[2] or l[0] == l[2]:
        print('Valido-Isoceles')
        print('Retangulo: ', end='')
        ret()
    else:
        print('Valido-Escaleno')
        print('Retangulo: ', end='')
        ret()
else:
    print('Invalido')
