l = [int(i) for i in str(input()).split()]

if l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
    print('S')
elif l[0] + l[1] == l[2] or l[0] + l[2] == l[1] or l[1] + l[2] == l[0]:
    print('S')
else:
    print('N')
