val = int(input())
print('{}'.format(val))
print('{} nota(s) de R$ 100,00'.format(val // 100))
print('{} nota(s) de R$ 50,00'.format((val % 100) // 50))

if (val % 100) // 50 > 0:
    print('{} nota(s) de R$ 20,00'.format((val % 100 - 50) // 20))
    if (val % 100-50) // 20 > 0:
        print('{} nota(s) de R$ 10,00'.format((val % 100 - 70) // 10))
    else:
        print('{} nota(s) de R$ 10,00'.format((val % 100 - 50) // 10))
else:
    print('{} nota(s) de R$ 20,00'.format((val % 100) // 20))
    if (val % 100) // 20 > 0:
        print('{} nota(s) de R$ 10,00'.format((val % 100 - 20) // 10))
    else:
        print('{} nota(s) de R$ 10,00'.format((val % 100) // 10))

print('{} nota(s) de R$ 5,00'.format((val % 10) // 5))

if (val % 10) // 5 > 0:
    print('{} nota(s) de R$ 2,00'.format((val % 10 - 5) // 2))
    if (val % 10-5) // 2 > 0:
        print('{} nota(s) de R$ 1,00'.format((val % 10 - 7) // 1))
    else:
        print('{} nota(s) de R$ 1,00'.format((val % 10 - 5) // 1))
else:
    print('{} nota(s) de R$ 2,00'.format((val % 10) // 2))
    if (val % 10) // 2 > 0:
        print('{} nota(s) de R$ 1,00'.format((val % 10 - 2) // 1))
    else:
        print('{} nota(s) de R$ 1,00'.format((val % 10) // 1))
