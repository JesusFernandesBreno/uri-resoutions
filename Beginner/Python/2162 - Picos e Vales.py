n = int(input())
med = [int(i) for i in str(input()).split()]
pv = 0
c = 0
vale = 0
pico = 0
while True:
    if c == n-1:
        break
    if med[c] > med[c+1]:
        pico += 1
        vale = 0
    elif med[c] < med[c+1]:
        vale += 1
        pico = 0
    else:
        vale += 1
        pico += 1
    c += 1

if vale == pico or vale > 1 or pico > 1:
    print(0)
else:
    print(1)
