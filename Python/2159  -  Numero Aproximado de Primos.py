from math import log
n = int(input())
p = n / log(n)
m = 1.25506 * p
print('{:.1f} {:.1f}'.format(p, m))
