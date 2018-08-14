resp = 1
idados = [0,0]
gdados = [0,0]
empates = 0
grenais = 0
igol = 0
ggol = 0

while resp != 2 and resp == 1:
    gols = str(input()).split()
    igol = int(gols[0])
    ggol = int(gols[1])

    if igol > ggol:
        idados[0] += 1
        gdados[1] += 1
    elif igol < ggol:
        idados[1] += 1
        gdados[0] += 1
    else:
        empates += 1

    grenais += 1
    
    resp = int(input('Novo grenal (1-sim 2-nao)\n'))

print('{} grenais'.format(grenais))
print('Inter:{}'.format(idados[0]))
print('Gremio:{}'.format(gdados[0]))
print('Empates:{}'.format(empates))

if idados[0] > gdados[0]:
    print('Inter venceu mais')
elif idados[0] < gdados[0]:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
    


