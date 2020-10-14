while True:
    val = str(input()).split(' ')
    if len(val) > 0:
        if val[0] == '0':
            break

    height = int(val[0])
    width = int(val[1])
    percent = int(val[2])

    house_area = height * width
    ground_area = (house_area * 100) // percent

    size_side = int(ground_area ** (1 / 2))

    print(size_side)
