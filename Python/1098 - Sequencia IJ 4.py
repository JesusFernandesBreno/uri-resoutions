import math
i = 0
j = 1

while i <= 2.0:
    if (i * 10 % 10) == 0 and (j * 10 % 10) == 0:
        for y in range(3):
            print('I={} J={}'.format(int(i),int(j+y)))
    else:
        for y in range(3):
            print('I={} J={}'.format(i,j+y))

    i += 0.2
    i = math.floor(i*100)/100
    j += 0.2
    j = math.floor(j*100)/100
