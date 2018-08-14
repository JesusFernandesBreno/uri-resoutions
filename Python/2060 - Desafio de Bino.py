n = int(input())
l = str(input()).split()
l = [int(i) for i in l]

m = [2,3,4,5]
mr = [0,0,0,0]
for i in l:
    for c, j in enumerate(m):
        if i % j == 0:
            mr[c] += 1
            
print('{} Multiplo(s) de 2'.format(mr[0]))
print('{} Multiplo(s) de 3'.format(mr[1]))
print('{} Multiplo(s) de 4'.format(mr[2]))
print('{} Multiplo(s) de 5'.format(mr[3]))
