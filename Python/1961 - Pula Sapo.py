t = str(input()).split()
seq = str(input()).split()
c = 0
while True:
    if abs(int(seq[c])-int(seq[c+1])) > int(t[0]):
        print('GAME OVER')
        break
    c += 1
    if c == (int(t[1])-1):
        print('YOU WIN')
        break
