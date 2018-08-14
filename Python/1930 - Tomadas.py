r = str(input()).split()
r  = [int(r[0]),int(r[1]),int(r[2]),int(r[3])]
s = 0
for i in r:
    s += i
print(s-3)
