while True:
    qtd = 0
    soma = 0
    n = int(input())
    if n == 0:
        break
    while True:
        if n % 2 == 0:
            soma += n
            qtd += 1

        n += 1
        
        if qtd == 5:
            break
    print(soma)
