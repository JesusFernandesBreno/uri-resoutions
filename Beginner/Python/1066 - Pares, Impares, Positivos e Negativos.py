n = [0,0,0,0,0]

n[0] = float(input())
n[1] = float(input())
n[2] = float(input())
n[3] = float(input())
n[4] = float(input())

qtd_par = 0
qtd_impar = 0
qtd_positivo = 0
qtd_negativo = 0
for i in n:
    if i % 2 == 0:
       qtd_par += 1
    if i % 2 == 1:
       qtd_impar += 1
    if i > 0:
        qtd_positivo += 1
    if i < 0:
        qtd_negativo += 1
       

print('{} valor(es) par(es)'.format(qtd_par))
print('{} valor(es) impar(es)'.format(qtd_impar))
print('{} valor(es) positivo(s)'.format(qtd_positivo))
print('{} valor(es) negativo(s)'.format(qtd_negativo))

