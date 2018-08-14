n = [0]*100
t = float(input())
i = 1
n[0] = t
while i < 100:
    n[i] = n[i-1]/2
    i += 1

i = 0  
while i < 100:
    print('N[{}] = {:.4f}'.format(i, n[i]))
    i += 1
