x = [0]*100
i = 0
while i < 100:
    x[i] = float(input())
    i += 1
    
i = 0
while i < 100:
    if x[i] <= 10:
        print('A[{}] = {}'.format(i, x[i]))
    i += 1


    
        
