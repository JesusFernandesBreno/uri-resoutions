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
            if j == 0:
                m_str += str(m[i][j]).rjust(3, ' ')
            else:
                m_str += str(m[i][j]).rjust(4, ' ')
        m_str += '\n'

    print(m_str)
