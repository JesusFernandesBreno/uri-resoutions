n = int(input())
for i in range(n):
    caso = str(input()).split()
    pa = int(caso[0])
    pb = int(caso[1])
    g1 = float(caso[2])
    g2 = float(caso[3])
    ano = 0
    while True:
        pa = pa + int((pa * (g1/100)))
        pb = pb + int((pb * (g2/100)))
        ano += 1
        if ano > 100:
            print('Mais de 1 seculo.')
            break
        elif pa > pb:
            print('{} anos.'.format(ano))
            break
