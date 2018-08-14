for i in range(int(input())):
    l = [str(input()).split() for i in range(3)]
    maior = float(l[2][0])
    menor = float(l[2][0])
    tot = 0
    for j in range(len(l[2])-1):
        if float(l[2][j+1]) > maior:
            maior = float(l[2][j+1])
        if float(l[2][j+1]) < menor:
            menor = float(l[2][j+1])
        tot += float(l[2][j])
        
    tot += float(l[2][6])
    tot -= (maior+menor)
    tot *= float(l[1][0])
    print('{} {:.2f}'.format(l[0][0],tot))

