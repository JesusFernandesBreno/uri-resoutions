ns =  input()

tot = 0
for i in ns:
    if i == '1':
        tot += 1
        
if tot % 2 == 0:
    print(ns+'0')
else:
    print(ns+'1')
