while True:
    try:
        d = [int(i) for i in str(input()).split()]
        dist = (((d[2]-d[0])**2) + ((d[3]-d[1])**2))**(1/2)#formula distancia

        if dist <= (d[5]+d[6]-(d[4]*1.5)):
            print('Y')
        else:
            print('N')
    except EOFError:
        break
