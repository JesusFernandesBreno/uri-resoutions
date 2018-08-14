while True:
    try:
        n = [int(i) for i in str(input()).split()]
        q = [int(input()) for i in range(n[0])]
        q = sorted(q, reverse=True)
        for i in range(n[1]):
            print(q[int(input())-1])
    except EOFError:
        break
