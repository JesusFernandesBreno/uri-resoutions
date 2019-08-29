cal = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
while True:
    try:
        data = str(input()).split()
        data = [int(i) for i in data]
        calc = cal[data[0]-1]+data[1]

        if calc == 359:
            print('E vespera de natal!')
        elif calc < 359:
            print('Faltam {} dias para o natal!'.format(360 - calc))
        elif calc > 360:
            print('Ja passou!')
        elif calc == 360:
            print('E natal!')
    except:
        break


