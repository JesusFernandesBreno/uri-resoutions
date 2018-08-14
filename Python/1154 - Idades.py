soma = 0
tot = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    tot += 1
print('{:.2f}'.format(soma/tot))
