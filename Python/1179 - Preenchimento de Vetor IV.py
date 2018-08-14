par = [0]*5
tam_p = 0
impar = [0]*5
tam_i = 0

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par[tam_p] = n
        tam_p += 1
        if tam_p > 4 :
            k = 0
            while k < 5:
                print('par[{}] = {}'.format(k, par[k]))
                k += 1
            tam_p = 0
    else:
        impar[tam_i] = n
        tam_i += 1
        if tam_i > 4:
            k = 0
            while k < 5:
                print('impar[{}] = {}'.format(k, impar[k]))
                k += 1
            tam_i = 0

k = 0
while k < tam_i:
    print('impar[{}] = {}'.format(k, impar[k]))
    k += 1

k = 0
while k < tam_p:
    print('par[{}] = {}'.format(k, par[k]))
    k += 1


    
        
