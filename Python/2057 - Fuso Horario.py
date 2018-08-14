hrs = str(input()).split()
hrs = [int(hrs[0]), int(hrs[1]), int(hrs[2])]
tot = hrs[0]+hrs[1]+hrs[2]

if tot < 23 and tot >= 0:
    print('{}'.format(tot))
elif tot < 0:
    print('{}'.format(tot+24))
else:
    print('{}'.format(tot-24))
