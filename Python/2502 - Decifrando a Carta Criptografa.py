while True:
    try:
        d1 = {}
        def descf():
            for i in msg:
                s = ''
                for j in i:
                    if j.upper() in d1:
                        if j.isupper():
                            s += d1[j.upper()]
                        else:
                            s += d1[j.upper()].lower()
                       
                    else:
                        s += j
                print(s)
                
               
        ns = [int(i) for i in str(input()).split()]
        cf = [input() for i in range(2)]
        for i in range(len(cf[0])):
            d1[cf[1][i]] = cf[0][i]
            d1[cf[0][i]] = cf[1][i]
        msg = [str(input()) for i in range(ns[1])]

        descf()
        print()
    except EOFError:
        break

