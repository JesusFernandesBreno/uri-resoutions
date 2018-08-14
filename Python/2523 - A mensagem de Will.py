while True:
    try:
        s = input()
        n = int(input())
        l = [int(i) for i in str(input()).split()]
        for i in l:
            print(s[i-1], end='')
        print()
    except EOFError:
        break
