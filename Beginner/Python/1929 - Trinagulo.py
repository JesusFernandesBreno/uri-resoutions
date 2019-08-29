v = str(input()).split()
v = [int(v[0]),int(v[1]),int(v[2]),int(v[3])]
c = 0
while True:
    d = 0
    if v[0] - v[2] < 0:
            d = -1*(v[0]-v[2])
    else:
            d = v[0]-v[2]
    c += 1
    
    if d < v[1] and v[1] < v[0] + v[2]:
        print('S')
        break
    elif c == 4:
        print('N')
        break
    v[0],v[1], v[2], v[3] = v[1],v[2], v[3], v[0]
