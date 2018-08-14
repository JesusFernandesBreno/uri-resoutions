n_alunos = int(input())
l_alunos = []
c = 0

while True:
    l_alunos.append(str(input()).split())
    c += 1
    if c == n_alunos:
        break
maior = []
maior.append(int(l_alunos[0][0]))
maior.append(float(l_alunos[0][1]))

for i in l_alunos:
    if float(i[1]) > maior[1] and float(i[1]) >= 8:
        maior[0] = int(i[0])
        maior[1] = float(i[1])

if maior[1] < 8:
    print('Minimum note not reached')
else:
    print(maior[0])
