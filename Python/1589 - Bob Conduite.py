t = int(input())
c = 0
while True:
    rs = str(input()).split()
    r1 = int(rs[0])
    r2 = int(rs[1])
    print('{}'.format(r1+r2))
    c += 1
    if c >= t:
        break
