n = int(input())
frase = 'LIFE IS NOT A PROBLEM TO BE SOLVED'

c = 0
while True:

    print(frase[c], end='')
    c += 1
    if n == c:
        print()
        break

