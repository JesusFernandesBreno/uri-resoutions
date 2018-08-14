first = [7]
second = [12,15,22,25,30,52,55,60,70]
third = [102,105,110,120,150]
while True:
    ns = str(input()).split()
    ns = [int(i) for i in ns]
    dif = ns[1] - ns[0]

    if ns[0] == 0 and ns[1] == 0:
        break
    
    if dif < 10:
        if dif in first:
            print('possible')
        else:
            print('impossible')
    elif dif < 100:
        second
        if dif in second:
            print('possible')
        else:
            print('impossible')
    else:
        if dif in third:
            print('possible')
        else:
            print('impossible')
    


