while True:
    try:
        ira = [[int(j) for j in str(input()).split()] for i in range(int(input()))]
        s_c_n = 0
        s_c = 0
        for i in ira:
            s_c_n += i[0]*i[1]
            s_c += i[1]
            
        calc = s_c_n/(s_c*100)
        print('{:.4f}'.format(calc))
    except EOFError:
        break

