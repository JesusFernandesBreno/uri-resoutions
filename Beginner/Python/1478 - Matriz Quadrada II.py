while True:
    order = int(input())
    if order == 0:
        break

    m = [[1]]

    for i in range(1, order):
        m[0].append(i + 1)

    for j in range(1, order):
        m.append([])
        m[j].append(j + 1)

    for i in range(1, order):
        for j in range(1, order):
            m[j].append(m[j-1][i-1])

    m_str = ''

    for i in range(order):
        for j in range(order):
            m_str += '{:>3d}'.format(m[i][j])
        m_str += '\n'

    print(m_str, end='')
