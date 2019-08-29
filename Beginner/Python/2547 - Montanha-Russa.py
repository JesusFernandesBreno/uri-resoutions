while True:
    try:
        n = [int(i) for i in str(input()).split()]
        a = [int(input()) for i in range(n[0])]

        tot = 0
        for i in a:
            if i >= n[1] and i <= n[2]:
                tot += 1
        print(tot)
    except EOFError:
        break
