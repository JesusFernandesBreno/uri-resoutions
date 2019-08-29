x = [0]*10
i = 0
n = int(input())
while i < 10:
    x[i] = n
    n *= 2
    i += 1
    
i = 0
while i < 10:
    print('N[{}] = {}'.format(i, x[i]))
    i += 1
