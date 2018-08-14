n = [0,0,0,0,0,0]

n[0] = float(input())
n[1] = float(input())
n[2] = float(input())
n[3] = float(input())
n[4] = float(input())
n[5] = float(input())

qtd = 0
tot = 0
for i in n:
    if i > 0:
       qtd += 1
       tot += i

print('{} valores positivos'.format(qtd))
print('{:.1f}'.format(tot/qtd))
