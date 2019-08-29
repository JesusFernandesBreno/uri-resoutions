while True:
    try:
        n = [int(i) for i in str(input()).split()]
        a = [0,0]
        p = [0,0]
        for c,i in enumerate(range(n[0])):
            
            ma = str(input()).split()
            if '1' in ma:
                a[0] = c
                a[1] = ma.index('1')
                
            if '2' in ma:
                p[0] = c
                p[1] = ma.index('2')
        n1 = abs(a[0]-p[0])
        n2 = abs(a[1]-p[1])
        print(n1+n2)    

    except EOFError:
        break

