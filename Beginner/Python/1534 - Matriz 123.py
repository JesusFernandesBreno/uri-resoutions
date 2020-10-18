while True:
    try:
        n = int(input())
        m = []
        a = 0
        b = n - 1

        m_str = ''

        for i in range(n):
            for j in range(n):
                if i == a and b == j:
                    m_str += '2'
                elif i == j:
                    m_str += '1'
                else:
                    m_str += '3'
            m_str += '\n'
            a += 1
            b -= 1

        print(m_str, end='')

    except EOFError:
        break
