n = int(input())
linha = ''
pri = 0
atual = 1

for i in range(1,n+1):
    for k in range(1,3):
        for j in range(1,4):
            prox = i * atual
            atual = prox
            if k == 2 and j != 1:
                linha += str(prox+1)
            else:
                linha += str(prox)
                
            if j != 3:
                linha += ' '
                
        print(linha)
        linha = ''
        atual = 1
     

