xs = str(input()).split()
ys = str(input()).split()
x1 = float(xs[0])
y1 = float(xs[1])
x2 = float(ys[0])
y2 = float(ys[1])

distancia = ( ( ( x2 - x1 ) ** 2 ) + ( ( y2 - y1 ) ** 2 ) ) ** ( 1 / 2)

print('{:.4f}'.format(distancia))
