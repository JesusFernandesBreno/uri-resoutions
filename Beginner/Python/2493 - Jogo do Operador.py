def op(op, n1, n2, n3):
    if op == '+':
        return (n1 + n2) == n3
    elif op == '-':
        return (n1 - n2) == n3
    elif op == '*':
        return (n1 * n2) == n3
    elif op == 'I':
        return (n1 + n2) != n3 and (n1 - n2 != n3) and (n1 * n2) != n3
        
while True:
    try:
        n = int(input())
        exp = [str(input()).split() for i in range(n)]
        e = [i[1].split("=") for i in exp]
        res = [str(input()).split() for i in range(n)]
        l_block= []
        for j in res:
            if not(op(j[2] ,int(exp[int(j[1])-1][0].split()[0]),int(e[int(j[1])-1][0]), int(e[int(j[1])-1][1]))) :
                l_block.append(j[0])
                
        if len(l_block) == n:
            print("None Shall Pass!")
        elif len(l_block) == 0:
            print("You Shall All Pass!")
        else:
            l_block = sorted(l_block)
            for c,i in enumerate(l_block):
                print(i, end='')
                if c != len(l_block)-1:
                    print('',end=" ")
                else:
                    print()
                
            
                
    except EOFError:
        break

