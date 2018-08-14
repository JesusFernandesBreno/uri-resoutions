vals = str(input()).split()
cod = int(vals[0])
qtd = int(vals[1])

if cod == 1:
      print('Total: R$ {:.2f}'.format(4.0*qtd))
elif cod == 2:
      print('Total: R$ {:.2f}'.format(4.5*qtd))
elif cod == 3:
      print('Total: R$ {:.2f}'.format(5.0*qtd))
elif cod == 4:
      print('Total: R$ {:.2f}'.format(2.0*qtd))
elif cod == 5:
      print('Total: R$ {:.2f}'.format(1.5*qtd))
