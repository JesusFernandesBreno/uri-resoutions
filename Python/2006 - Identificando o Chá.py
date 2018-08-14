tipo = int(input())
resp = str(input()).split()

tot = 0
for i in resp:
    if int(i) == tipo:
        tot += 1

print(tot)
