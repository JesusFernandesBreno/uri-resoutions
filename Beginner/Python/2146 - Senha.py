while True:
    try:
        senha = int(input())
        print('{}'.format(senha-1))
    except EOFError:
        break
