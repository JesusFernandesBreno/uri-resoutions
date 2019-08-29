n1 = int(input())
n2 = int(input())

maior = 0
menor = 0
if n1 < n2 or n1 == n2:
    menor = n1
    maior = n2
elif n1 > n2:
    menor = n2
    maior = n1


for n in range(menor+1, maior):
    if n % 5 == 2 or n % 5 == 3:
        print(n)
