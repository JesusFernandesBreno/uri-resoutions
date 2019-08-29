n = [0]*1000
t = int(input())
i = 0
while True:
    for j in range(t):
        if i == 1000:
            break
        n[i] = j
        i += 1
    if i == 1000:
            break

i = 0  
while i < 1000:
    print('N[{}] = {}'.format(i, n[i]))
    i += 1
