v = float(input())

if v >= 0 and v <= 2000:
    print('Isento')
elif v >= 2000.01 and v <= 3000:
    print('R$ {:.2f}'.format((v-2000)*0.08))
elif v >= 3000.1 and v <= 4500:
    print('R$ {:.2f}'.format((999.99*0.08)+((v-2999.99)*0.18)))
else:
    print('R$ {:.2f}'.format((999.99*0.08)+(1499.99*0.18)+((v-4500)*0.28)))
    
