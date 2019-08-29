while True:
    n = [int(i) for i in str(input()).split()]
    if n[0] == 0 and n[1] == 0:
        break
    print('{}'.format(n[0]*n[1]))
