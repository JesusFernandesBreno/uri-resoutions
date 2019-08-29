while True:
    try:
        qtd = int(input())
        
        lesmas = str(input()).split()
        lesmasInt = []
        for y in lesmas:
            lesmasInt.append(int(y))
        
        maior = 0
        for x in lesmasInt:
            if x > maior:
                maior = x
        if maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
        
