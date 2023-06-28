# Probandop àmbitos

titulo = 'Probando àmbitos'
suma = 10.5

def sumar():
    suma = 2 + 2
    print(titulo)
    print('suma en àmbito local',suma, id(suma))
    
print('Antes de llamar a la funciòn')
print('suma en ambito global',suma,id(suma))
sumar()
print ('Despues de llamar a la funciòn sumar')
print('suma en el àmbito global',suma,id(suma))
