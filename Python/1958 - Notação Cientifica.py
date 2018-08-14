num = input()
m = num[0]
dec = float(num)
if dec > 0:
    print('+{:.4E}'.format(dec))
elif dec == 0:
    if m == '-':
        print('{:.4E}'.format(dec))
    else:
        print('+{:.4E}'.format(dec))
else:
    print('{:.4E}'.format(dec))
