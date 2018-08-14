n = int(input())
fib = [0]*61
for i in range(n):
    caso = int(input())
    fib[0] = 0
    fib[1] = 1
    i = 2
    while i != 61:
        fib[i] = fib[i-1] + fib[i-2]
        i += 1
    
    print('Fib({}) = {}'.format(caso,fib[caso]))
