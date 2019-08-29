while True:
    try:
        n_a = int(input())
        n_c = [int(i) for i in str(input()).split()]
        m_c_a = [[int(j) for j in str(input()).split()] for i in range(n_c[0])]
        l_c_a = [[int(j) for j in str(input()).split()] for i in range(n_c[1])]
        c_e = [int(i) for i in str(input()).split()]
        col = int(input())

        if m_c_a[c_e[0]-1][col-1] > l_c_a[c_e[1]-1][col-1]:
            print('Marcos')
        elif m_c_a[c_e[0]-1][col-1] < l_c_a[c_e[1]-1][col-1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break
