numc = 1
while True:
    try:
        nmax = int(input())
        n = 0
        c = 0
        s = ''
        ns = ''
        
        tot = 0
        if nmax == 0:
            ns = 'numero'
        else:
            ns = 'numeros'
            
        while True:
            
            s += str(n)
            
            if c == n:
                n += 1
                c = 0
                
            c += 1
            tot += 1
            if nmax+1 == n:
                print('Caso {}: {} {}'.format(numc , tot, ns))
                print(s+'\n')
                numc += 1
                break
            
            s += ' ' 
    except EOFError:
        break

