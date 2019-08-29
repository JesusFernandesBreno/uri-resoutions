dim = [int(i) for i in str(input()).split()]
ma = [[int(j) for j in str(input()).split()] for i in range(dim[0])]
maxh = dim[0]-1
maxv = dim[1]-1

def verifica(c1, c2):
    for i in range(3):
        for j in range(3):
            if i != 1 and j != 1:
                if ma[c1+i-1][c2+j-1] != 7:
                    return False
                    
    return True

c1 = 1
c2 = 1
achou = False
while c1 < maxh and not achou: 
    while c2 < maxv and not achou:
        if ma[c1][c2] == 42:
            achou =  verifica(c1, c2)
            if achou:
                print(c1+1, c2+1)
        c2 += 1
    c2 = 1
    c1 += 1
    
if not achou:
    print('0 0')
