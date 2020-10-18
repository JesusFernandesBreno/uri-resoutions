while True:
    order = int(input())
    if order == 0:
        break

    power = 0
    last_power = 0
    m = []

    for i in range(0, order):
        m.append([])
        power = last_power
        for j in range(order):
            m[i].append(2 ** power)
            power += 1
        last_power += 1

    m_str = ''
    len_max_number = len(str(m[order -1][order - 1]))
    for i in range(order):
        for j in range(order):
            if j == 0:
                m_str += str(m[i][j]).rjust(len_max_number, ' ')
            else:
                m_str += str(m[i][j]).rjust(len_max_number + 1, ' ')
        m_str += '\n'

    print(m_str)
