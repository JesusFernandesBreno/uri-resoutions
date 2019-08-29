ns = str(input()).split()
a = int(ns[0])
b = int(ns[1])
r = 0
q = 0
if  b < 0:
    r = a%(b*-1)
    q = -1*(a // (b*-1))
else:
    r = a%b
    q =  a//b

print('{} {}'.format(q, r ))
