n = int(input())
n_m = int(input())
l = [int(input()) for i in range(n)]
l = sorted(l,reverse=True)
tot = 0
for i in l[n_m:]:
    if i == l[n_m-1]:
        tot += 1
        
print(tot+n_m)
