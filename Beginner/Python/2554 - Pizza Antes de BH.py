while True:
    try:
        n = [int(i) for i in str(input()).split()]
        ds = [str(input()).split() for i in range(n[1])]
        tot = 0
        l = []
        for c,i in enumerate(ds):
            for j in i:
                if j == '1':
                    tot += 1
            if tot == n[0]:
                l.append(c)
            tot = 0
        if len(l) == 0:
            print('Pizza antes de FdI')
        elif len(l) == 1:
            print(ds[l[0]][0])
        else:
            ls = []
            m_ano = int(ds[l[0]][0].split('/')[2])
            for k in l:
                ls = ds[k][0].split('/') 
                if int(ls[2]) < m_ano:
                    l.remove(k)
            if len(l) == 1:
                print(ds[l[0]][0])
            else:
                ls = []
                m_mes = int(ds[l[0]][0].split('/')[1])
                for k in l:
                    ls = ds[k][0].split('/') 
                    if int(ls[2]) < m_ano:
                        l.remove(k)
                if len(l)== 1:
                    print(ds[l[0]][0])
                else:
                    ls = []
                    m_dia = int(ds[l[0]][0].split('/')[0])
                    for k in l:
                        ls = ds[k][0].split('/') 
                        if int(ls[2]) < m_ano:
                            l.remove(k)
                    print(ds[l[0]][0])
    
                            
                        
    except EOFError:
        break
