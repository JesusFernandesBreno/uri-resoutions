vals = str(input()).split()
for i in range(3):
      vals[i] = float(vals[i])

vals.sort()

a = vals[2]
b = vals[1]
c = vals[0]

if a >= b + c:
      print('NAO FORMA TRIANGULO')
else:
      if a**2 == b**2 + c**2:
            print('TRIANGULO RETANGULO')
      if a**2 > b**2 + c**2:
            print('TRIANGULO OBTUSANGULO')
      if a**2 < b**2 + c**2:
            print('TRIANGULO ACUTANGULO')
      if a == b and a == c:
            print('TRIANGULO EQUILATERO')
      elif a == b or b==c or a == c:
            print('TRIANGULO ISOSCELES')
