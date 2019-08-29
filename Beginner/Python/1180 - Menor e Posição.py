n = int(input())
v = str(input()).split()

i = 1
menor = int(v[0])
posicao = 0
while i < n:
    if int(v[i]) < menor:
        menor = int(v[i])
        posicao = i
    i += 1
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))
