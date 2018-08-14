salario = float(input())

if  salario >= 0 and salario <= 400.00:
      print('Novo salario: {:.2f}'.format(salario+(salario*0.15)))
      print('Reajuste ganho: {:.2f}'.format((salario*0.15)))
      print('Em percentual: {} %'.format(15))


elif salario >= 400.01 and salario <= 800.00:
      print('Novo salario: {:.2f}'.format(salario+(salario*0.12)))
      print('Reajuste ganho: {:.2f}'.format((salario*0.12)))
      print('Em percentual: {} %'.format(12))
      
elif salario >= 800.01 and salario <= 1200.00:
      print('Novo salario: {:.2f}'.format(salario+(salario*0.10)))
      print('Reajuste ganho: {:.2f}'.format((salario*0.10)))
      print('Em percentual: {} %'.format(10))
      

elif salario >= 1200.01 and salario <= 2000.00:
      print('Novo salario: {:.2f}'.format(salario+(salario*0.07)))
      print('Reajuste ganho: {:.2f}'.format((salario*0.07)))
      print('Em percentual: {} %'.format(7))

else:
      print('Novo salario: {:.2f}'.format(salario+(salario*0.04)))
      print('Reajuste ganho: {:.2f}'.format((salario*0.04)))
      print('Em percentual: {} %'.format(4))
