while True:
    n = input()
    if len(n) == 0:
        break
    else:
        n = int(n)
        if n == 0:
            break
        
    for i in range(1,n+1):
        if i != n:
            print('{}'.format(i), end=" ")
        else:
            print('{}'.format(i))
