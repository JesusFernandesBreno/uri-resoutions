n = int(input())
c = 0
while True:
    a = int(input())
    if a < 2015:
        print(str(2015-a)+' D.C.')
    elif a == 2015:
        print('1 A.C.')
    else:
        print(str(a-2015+1)+' A.C.')
    c += 1
    if c == n:
        break
