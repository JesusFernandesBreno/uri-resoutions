def adj(x,y):
    tot = 0
    if x >= 0 and x < n[0]-1:
        if m[x+1][y] == 9:
            tot += 1
    if x > 0 and x <= n[0]-1:
        if m[x-1][y] == 9:
            tot += 1
            
    if y >= 0 and y < n[1]-1:
        if m[x][y+1] == 9:
            tot += 1

    if y > 0 and y <= n[1]:
        if m[x][y-1] == 9:
            tot += 1

    return tot
        
    
    
while True:
    try:
        n = [int(i) for i in str(input()).split()]
        m = [[int(j) for j in str(input()).split()] for i in range(n[0])]
        for c1,i in enumerate(m):
            for c2,j in enumerate(i):
                if j == 1:
                    m[c1][c2] = 9
