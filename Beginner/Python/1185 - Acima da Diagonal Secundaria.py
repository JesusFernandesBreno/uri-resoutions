m = [[0]*12 for i in range(12)]

t = input()
i = 0
k = 0

while i < 12:
    while k < 12:
        m[i][k] = float(input())
        k += 1
    i += 1
    k = 0

i = 0
soma = 0
k = 0
qtd = 0
while i < 12:
    while k < 12:
        if ( i + k) < 11:
            soma += m[i][k]
            qtd += 1
        k += 1
    i += 1
    k = 0
        
    
if t == 'S':
    print('{:.1f}'.format(soma))
elif t == 'M':
    print('{:.1f}'.format(soma/qtd))
