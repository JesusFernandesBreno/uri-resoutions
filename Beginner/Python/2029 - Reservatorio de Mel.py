while True:
    try:
        m = [float(input()),float(input())]
        PI = 3.14
        volume = m[0]
        raio = (m[1]/2)**2
        print('ALTURA = {:.2f}'.format(volume/(PI*raio)))
        print('AREA = {:.2f}'.format(PI*raio))
    except EOFError:
        break
