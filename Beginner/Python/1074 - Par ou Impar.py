n = int(input())
lista = []
for i in range(n):
    new = int(input())
    lista.append(new)

for i in lista:
    if i == 0:
        print('NULL')
    elif i > 0 and i % 2 == 0:
        print('EVEN POSITIVE')
    elif i > 0 and i % 2 == 1:
        print('ODD POSITIVE')
    elif i < 0 and i % 2 == 0:
        print('EVEN NEGATIVE')
    elif i < 0 and i % 2 == 1:
        print('ODD NEGATIVE')
