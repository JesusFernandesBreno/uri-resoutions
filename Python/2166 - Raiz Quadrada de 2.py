n = int(input())
ant = 1
if n > 1:
    ant = 2+1/2
    for i in range(n-2):
        t = 2 + 1/ant
        ant = t
    pos = 1/ant
elif n == 1:
    pos = 1/2
else:
    pos = 0
print('{:.10f}'.format(1 + pos))
