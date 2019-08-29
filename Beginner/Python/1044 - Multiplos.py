vals = str(input()).split()
a = int(vals[0])
b = int(vals[1])

if (a % b == 0) or (b % a == 0):
      print('Sao Multiplos')
else:
      print('Nao sao Multiplos')
