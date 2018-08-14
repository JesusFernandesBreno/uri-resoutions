c =  str(input()).split()
c = [int(c[0]), int(c[1])]

if c[0] == c[1]:
    print(c[0])
else:
    if c[0] > c[1]:
        print(c[0])
    else:
        print(c[1])
