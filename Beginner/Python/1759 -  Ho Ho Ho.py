n = int(input())
linha =  ''

i = 0
while True:
    linha += "Ho"
    i += 1
    if i == n:
        linha += "!"
        break
    else:
        linha += " "

print(linha)
