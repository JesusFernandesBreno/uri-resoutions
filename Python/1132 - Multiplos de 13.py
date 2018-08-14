n1 = int(input())
n2 = int(input())

n = 0
soma = 0
maior = 0
menor = 0
if n1 < n2 or n1 == n2:
    menor = n1
    maior = n2
elif n1 > n2:
    menor = n2
    maior = n1


for n in range(menor, maior+1):
    if n % 13 != 0:
        soma += n
        
print(soma)
