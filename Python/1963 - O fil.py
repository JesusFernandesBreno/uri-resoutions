v = str(input()).split()
v = [float(v[0]), float(v[1])]
print('{:.2f}%'.format((v[1]-v[0])/v[0]*100))
