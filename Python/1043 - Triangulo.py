vals = str(input()).split()
a = float(vals[0])
b = float(vals[1])
c = float(vals[2])

if (a + b > c) and (b + c > a) and (a + c > b):
      print('Perimetro = {:.1f}'.format(a+b+c))
else:
      print('Area = {:.1f}'.format(((a+b)*c)/2))
