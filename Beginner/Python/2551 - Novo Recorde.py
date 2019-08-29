while True:
    try:
        n = [[int(j) for j in str(input()).split()] for i in range(int(input()))]
        rec = 0
        for c,i in enumerate(n):
            if rec < i[1]/i[0]:
                rec = i[1]/i[0]
                print(c+1)
        
    except EOFError:
        break
