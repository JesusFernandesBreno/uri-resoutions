mn = str(input()).split()
m = int(mn[0])
n = int(mn[1])
a = [input() for i in range(n)]

for i in a:
    if i == 'clicou':
        m -= 1
    else:
        m += 1
print(m)
