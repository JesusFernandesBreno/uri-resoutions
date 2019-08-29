n = int(input())
ns = [int(i) for i in str(input()).split()]

def pos():
    c = 0
    while c < n-1:
        if ns[c] > ns[c+1]:
            return c+2
        c += 1
    return 0

print(pos())
