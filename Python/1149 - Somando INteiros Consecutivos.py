an = str(input()).split()
c = 0
while c < len(an):
    if c == 0:
        a = int(an[0])
    elif c > 0 and int(an[c]) > 0:
        n = int(an[c])
        soma = 0
        for i in range(n):
            soma += i + a

        print(soma)
        
    c += 1
