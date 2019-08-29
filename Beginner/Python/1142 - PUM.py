n = int(input())
acrs = 0
linha = ''
for i in range(n):
    for j in range(1,4):
        linha += str(j+acrs)+" "
    print(linha + 'PUM')
    acrs += 4
    linha = ''
