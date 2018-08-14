testes = int(input())
cont = 0
while True:
    qtd = int(input())
    a = 1
    b = -1
    aux = 0

    s = 0
    c = 0
    while True:
        s += a
        a, b = b, a
        c += 1
        if c == qtd:
            print(s)
            break
    cont += 1
    if testes == cont:
        break
    
