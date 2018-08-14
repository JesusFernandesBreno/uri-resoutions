n = int(input())
for i in range(n):
    n1 = int(input())
    soma = 0
    for j in range(1,n1):
        if n1 % j == 0:
            soma += j
    if soma == n1:
        print('{} eh perfeito'.format(n1))
    else:
        print('{} nao eh perfeito'.format(n1))
