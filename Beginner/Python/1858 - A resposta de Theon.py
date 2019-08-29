n = int(input())

l = str(input()).split()

c = 0
menor = int(l[0])
nmenor = 1
while True:
    if int(l[c]) < menor:
        menor = int(l[c])
        nmenor = c+1
    c += 1
    if c  == n :
        break
print(nmenor)
