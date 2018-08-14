l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break
print(len(set(l)))
