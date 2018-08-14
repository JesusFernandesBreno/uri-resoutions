notas = []
while True:
    entrada = float(input())

    
    if entrada > 0 and entrada <= 10 :
        if len(notas) <= 2:
            notas.append(entrada)
            if len(notas) == 2:
                print('media = {:.2f}'.format((notas[0]+notas[1])/2))
                break
    else:
        print('nota invalida')


        
