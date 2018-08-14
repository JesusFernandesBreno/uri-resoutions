while True:
  try:
    while True:
        hr = input()
        if int(hr[0]) < 7:
            print('Atraso maximo: 0'.format(int(hr[0])))
        elif int(hr[0]) == 7:
            if int(hr[2:4]) > 0:
                print('Atraso maximo: {}'.format(int(hr[2:4])))
            else:
                print('Atraso maximo: 0'.format(int(hr[0])))
        elif int(hr[0]) >= 8:
            print('Atraso maximo: {}'.format(((int(hr[0])-8)*60)+int(hr[2:4])+60))
  except EOFError:
    break
