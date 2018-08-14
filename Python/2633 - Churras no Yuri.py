while True:
    try:
        n = int(input())
        l = []
        a = ''
        for i in range(n):
            a = str(input()).split()
            l.append([int(a[1]),a[0]])
        l = sorted(l)
        for c,j in enumerate(l):
            print(j[1],end='')
            if c < len(l)-1:
                print(end=' ')
            else:
                print()
    except EOFError:
        break
