segundos  = int(input())
horas = segundos // 3600
minutos = 0

if horas == 0:
      minutos = segundos // 60
            
else:
      minutos = (segundos - horas * 3600)//60

print('{}:{}:{}'.format(horas, minutos,segundos-(horas*3600+minutos*60))) 
      

