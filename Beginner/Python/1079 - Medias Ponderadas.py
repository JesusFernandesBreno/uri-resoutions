n = int(input())

caso = []
lista_medias = []
for i in range(n):
    caso = str(input()).split()
    n1 = float(caso[0])
    n2 = float(caso[1])
    n3 = float(caso[2])
    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    lista_medias.append(media)

for i in lista_medias:
    print('{:.1f}'.format(i))
