while True:
    try:
        n = int(input())
        c = n
        v = -1
        while c > 0:
            c = c//2
            v += 1
        print(v)
    except EOFError:
        break
