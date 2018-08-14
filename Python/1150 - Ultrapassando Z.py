x = int(input())

while True:
    z = int(input())
    if z > x:
        break

soma = x
quant = 1
prox = 0
while soma < z:
    soma += prox
    prox += x+1
    quant += 1

print(quant)
