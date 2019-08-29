n = int(input())
linha = ''
pri = 0
atual = 1

for i in range(1,n+1):
    
    for j in range(1,4):
        prox = i * atual
        atual = prox    
        linha += str(prox)
        if j != 3:
            linha += ' '
            
    print(linha)
    linha = ''
    atual = 1
