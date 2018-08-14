idade = int(input())
ano = idade // 365
mes = (idade % 365) // 30
dia = (idade % 365) % 30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
