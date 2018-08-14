n = int(input())
lista = []
tot_in = 0
tot_out = 0
for x in range(n):
    new = int(input())
    lista.append(new)
    if new >= 10 and new <= 20:
        tot_in += 1
    else:
        tot_out += 1

print('{} in'.format(tot_in))
print('{} out'.format(tot_out))
