vals = str(input()).split()
a = float(vals[0])
b = float(vals[1])
c = float(vals[2])

delta = (b**2) - (4*a*c)
r1 = 0
r2 = 0
if delta < 0:
      print('Impossivel calcular')
else:
      r1 = (-b + delta**(1/2))
      r2 = (-b - delta**(1/2))
      if r1 == 0 or r2 == 0:
            print('Impossivel calcular')
      else:
            r1 = r1/(2*a)
            r2 = r2/(2*a)
            print('R1 = {:.5f}'.format(r1))
            print('R2 = {:.5f}'.format(r2))
