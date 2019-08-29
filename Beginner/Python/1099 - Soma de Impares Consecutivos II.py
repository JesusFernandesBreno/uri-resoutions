casos = int(input())

lista = []
for i in range(casos):
    x = str(input()).split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    lista.append(x)

for x in lista:
    if x[0] < x[1]:
        a = x[0]
        b = x[1]
        tot = 0
        while a != b:
            a += 1
            if a % 2 != 0 and a != b:
                tot += a
        print(tot)
                
    else:
        a = x[0]
        b = x[1]
        tot = 0
        while b != a:
            b += 1
            if b % 2 != 0 and b != a:
                tot += b
        print(tot)
