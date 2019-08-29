n = int(input())
c = int()
while c < n :
    ns = str(input()).split()
    
    n1 = int(ns[0])
    n2 = int(ns[1])

    try:
        print('{}'.format(n1/n2))
    except ZeroDivisionError:
        print('divisao impossivel')
    c += 1
