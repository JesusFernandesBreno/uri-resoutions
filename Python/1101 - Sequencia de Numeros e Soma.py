lista = []

while True:
    ab = str(input()).split()
        
           
    if len(ab) == 2:
        ab[0] = int(ab[0])
        ab[1] = int(ab[1])
        if ab[0] > 0 and ab[1] > 0:
            lista.append(ab)
        else:
            break
    else:
        break

out = ''
l = []
tot = 0
for x in lista:
    if x[0] < x[1]:
        x[0], x[1] = x[1], x[0]
        
    for y in range(x[1], x[0]+1):
        out += str(y)+' '
        tot += y
    l.append(out+'Sum='+str(tot))
    out = ''
    tot = 0

for y in l:
    print(y)
