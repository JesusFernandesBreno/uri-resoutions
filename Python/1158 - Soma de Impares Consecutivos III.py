n = int(input())

for i in range(n):
    ns = str(input()).split()
    n1 = int(ns[0])
    qtd = int(ns[1])

    soma = 0
    i = 0

    while True:
        if n1 % 2 == 1:
            soma += n1
            i += 1
        
        n1 += 1
        if i == qtd:
            break
        
    print(soma)
