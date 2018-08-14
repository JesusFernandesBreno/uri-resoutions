j = 8
for i in range(1,10):
    for y in range(1,4):
        if i % 2 == 1:
            print('I={} J={}'.format(i,j-y))
    j += 1
