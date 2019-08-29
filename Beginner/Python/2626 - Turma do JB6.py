p = ['pedra','papel']

def vs(x,y):
            if x == p[0]:
                if y == p[1]:
                    return False
                elif y == p[0]:
                    return None
                else:
                    return True

            elif x == p[1]:
                if y == p[1]:
                    return None
                elif y == p[0]:
                    return True
                else:
                    return False

            else:
                if y == p[1]:
                    return True
                elif y == p[0]:
                    return False
                else:
                    return None
while True:
    try:
        l = [i for i in str(input()).split()]
