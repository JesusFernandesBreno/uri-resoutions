n1 = int(input())
n2 = int(input())

tot = 0
if n1 < n2:
    for i in range(n1,n2):
        if i % 2 == 1 and i != n1:
            tot += i
    print(tot)
elif n1 > n2:
    for i in range(n1,n2,-1):
        if i % 2 == 1 and i != n1:
            tot += i
    print(tot)
else:
    print(0)


