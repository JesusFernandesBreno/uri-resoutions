while True:
    cord_str = str(input())
    cord = cord_str.split()

    if len(cord) != 2:    
        break
    
    c1 =  int(cord[0])
    c2 = int(cord[1])

    if c1 > 0 and c2 > 0:
        print('primeiro')
    elif c1 > 0 and c2 < 0:
        print('quarto')
    elif c1 < 0 and c2 < 0:
        print('terceiro')
    elif c1 < 0 and c2 > 0:
        print('segundo')
    else:
        break
    
