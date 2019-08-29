lista = []
while True:
    a = str(input()).split()
    a[0] = int(a[0])
    a[1] = int(a[1])

    if a[0] == a[1]:
        break
    else:
        lista.append(a)

for x in lista:
    if x[0] > x[1]:
        print('Decrescente')
    elif x[0] < x[1]:
        print('Crescente')
    
   
    
    
