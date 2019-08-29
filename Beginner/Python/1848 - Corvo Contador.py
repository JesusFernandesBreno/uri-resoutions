c = 0
tot = 0
while True:
    
    l = input()
    if l == 'caw caw':
        print(tot)
        c += 1
        tot = 0
    else:
        
        if l[0] == '*':
            tot += 4
            if l[1] == '*':
                tot += 2
                if l[2] == '*':
                    tot += 1
            elif l[2] == '*':
                tot += 1
        elif l[1] == '*':
            tot += 2
            if l[2] == '*':
                tot += 1
        elif l[2] == '*':
            tot += 1
    
    if c == 3:
        break
