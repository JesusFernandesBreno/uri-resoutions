qtd = int(input())

n1 = 0
n2 = 1
aux = 0
linha = ''
i = 0
while True:
    
    linha += str(n1)
    i += 1
    n1 += n2
    if i == qtd:
        break
    else:
        linha += " "
    linha += str(n2)
    i += 1
    n2 += n1
    if i == qtd:
        break
    else:
        linha += " "
print(linha)
