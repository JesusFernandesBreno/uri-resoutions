while True:
    n = int(input())
    if n == 0:
        break
    c = 0
    while True:
        p = int(input())
        if p % 2 == 0:
            print('{}'.format(p*2-2))
        else:
            print('{}'.format(p*2-1))
        c += 1
        if c == n:
            break

