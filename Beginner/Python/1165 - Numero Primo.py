n = int(input())
for i in range(n):
    n1 = int(input())
    div = False
    for j in range(2,n1):
        if n1 % j == 0:
            div = True
            break
        
    if not div:
        print('{} eh primo'.format(n1))
    else:
        print('{} nao eh primo'.format(n1))
