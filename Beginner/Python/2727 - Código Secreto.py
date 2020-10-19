while True:
    try:
        qtd = int(input())

        result = ''
        for i in range(qtd):
            char_encoded = str(input()).split(' ')

            ascii_char = 96

            count = 0

            ascii_char += len(char_encoded[0]) + (3 * (len(char_encoded) - 1))

            result += f'{chr(ascii_char)}\n'

        print(result, end='')

    except EOFError:
        break
