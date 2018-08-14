vals = str(input()).split()
a = int(vals[0])
b = int(vals[1])
c = int(vals[2])
d = int(vals[3])

if a < c:
      minutos_tot = ((c - a) * 60) - b + d
      print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(minutos_tot//60,minutos_tot%60))
else:
      minutos_tot = ((24-a)+c)*60 - b + d
      print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(minutos_tot//60,minutos_tot%60))
