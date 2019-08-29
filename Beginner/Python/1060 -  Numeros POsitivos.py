n = [0,0,0,0,0,0]

n[0] = float(input())
n[1] = float(input())
n[2] = float(input())
n[3] = float(input())
n[4] = float(input())
n[5] = float(input())

tot = 0
for x in n:
    if x > 0:
        tot += 1
print('{} valores positivos'.format(tot))
