import datetime

edad = int(input("¿Que edad tienes? "))

if edad > 0:
  if edad >= 18:
    print('Por ahora no hay nada que hacer')
  else:
    if datetime.datetime.now().hour <= 18:
      print('Tienes que hacer la tarea')
    else:
      print('Es hora de ir a dormir')
else:
  print('Ingresar una edad mayor')