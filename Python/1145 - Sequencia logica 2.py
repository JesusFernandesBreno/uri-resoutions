ns = str(input()).split()
n1 = int(ns[0])
n2 = int(ns[1])
line = ''
for i in range(1,n2+1):
    if line == '':
        line = line + str(i)
    else:
        line = line + ' ' + str(i)
    if i % n1 == 0:
        print(line)
        line = ''

    
