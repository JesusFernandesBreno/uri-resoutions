l = [int(input()) for i in range(3)]
tot = 0
t = 0
for c,i in enumerate(l):
        if c != 0:
            tot += 2*(abs(0 - c)*i)

for j in range(1,3):
    for c,i in enumerate(l):
        if c != j:
            t += 2*(abs(j - c)*i)
    
    if t < tot:
        tot = t
    t = 0

print(tot)
