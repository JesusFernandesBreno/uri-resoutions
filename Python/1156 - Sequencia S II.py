s = 1
n = 3
d = 2

while True:
    s += n/d
    d *= 2
    n += 2
    if n > 39:
        break
    
print('{:.2f}'.format(s))
