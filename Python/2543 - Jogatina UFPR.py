while True:
    try:
        n = [int(i) for i in str(input()).split()]
        ns = [[int(j) for j in str(input()).split()]for i in range(n[0])]
        tot = 0
        for i in ns:
            if i[0] == n[1] and i[1]==0:
                tot += 1
        print(tot)
    except EOFError:
        break
