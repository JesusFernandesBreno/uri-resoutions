vals = str(input()).split()
vals_backup = [0,0,0]
for i in range(3):
      vals[i] = int(vals[i])
      vals_backup[i] = int(vals[i])
vals.sort()
for x in vals:
      print(x)
print()
for x in vals_backup:
      print(x)

