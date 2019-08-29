m = [[0]*12 for i in range(12)]

l = int(input())
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
while i < 12:
    soma += m[l][i]
    i += 1
    
if t == 'S':
    print('{:.1f}'.format(soma))
elif t == 'M':
    print('{:.1f}'.format(soma/12))
