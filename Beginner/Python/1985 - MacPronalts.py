precos = {1001:1.5, 1002:2.5, 1003:3.5, 1004:4.5, 1005:5.5}
n_prod = int(input())
c = 0
pedido = []
while True:
    pedido.append(str(input()).split())
    c += 1
    if c == n_prod:
        break


tot = 0
for i in pedido:
    tot += int(i[1]) * precos[int(i[0])]
print('{:.2f}'.format(tot))
