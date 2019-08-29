n = int(input())
ma =[[int(j) for j in str(input()).split()] for i in range(n+1)]

def verifica(c1, c2):
    b = 0
    for i in range(0,2):
        for j in range(0,2):
            if ma[c1+i][c2+j] == 1:
                b += 1
                if b == 2:
                    return True
    return False
                
c1 = 0
c2 = 0
