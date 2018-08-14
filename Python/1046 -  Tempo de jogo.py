vals = str(input()).split()
a = int(vals[0])
b = int(vals[1])

if a < b:
      print('O JOGO DUROU {} HORA(S)'.format(b-a))
else:
     print('O JOGO DUROU {} HORA(S)'.format((24-a)+b)) 
