teste = int(input())
c1 = 0

while True:
    p = [str(input()).split(),str(input()).split()]
    ni = []
    if len(p[1]) == 2:
        ni = [int(p[1][0]),int(p[1][1])]
        s = ni[0] + ni[1]
        if s % 2 == 0:
            if p[0][1] == 'PAR':
                print(p[0][0])
            else:
                print(p[0][2])
        else:
            if p[0][1] == 'IMPAR':
                print(p[0][0])
            else:
                print(p[0][2])
                      
    
    c1 += 1
    if c1 == teste:
        break
