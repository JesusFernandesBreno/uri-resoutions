temps = str(input()).split()

t = [0,0,0]
t[0] = int(temps[0])
t[1] = int(temps[1])
t[2] = int(temps[2])

if t[0] > t[1] and t[1] <= t[2]:
    print(':)')
elif t[0] < t[1] and t[1] >= t[2]:
    print(':(')
elif t[0] < t[1] and t[1] < t[2] and (t[1] - t[0]) > (t[2] - t[1]):
    print(':(')
elif t[0] < t[1] and t[1] < t[2] and (t[1] - t[0]) <= (t[2] - t[1]):
    print(':)')
elif t[0] > t[1] and t[1] > t[2] and (t[1] - t[0]) < (t[2] - t[1]):
    print(':)')
elif t[0] > t[1] and t[1] > t[2] and (t[1] - t[0]) >= (t[2] - t[1]):
    print(':(')
elif t[0] == t[1] and t[1] < t[2]:
    print(':)')
elif t[0] == t[1] and t[1] >= t[2]:
    print(':(')
