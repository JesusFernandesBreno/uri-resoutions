x = [0]*10
i = 0
while i < 10:
    x[i] = int(input())
    i += 1
    
i = 0
while i < 10:
    if x[i] <= 0:
        x[i] = 1
    i += 1

i = 0
while i < 10:
    print('X[{}] = {}'.format(i, x[i]))
    i += 1


    
        
