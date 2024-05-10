import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

i = 0
suma = 0
cantidad = input('Cantidad de notas: ')
pos = cantidad.find('.')
if pos != -1:
    print('Chaooo')
else:
    if cantidad.isnumeric() == 'False':
        print('Chaoo')
    else:
        cantidad = int(cantidad)
        
while i < cantidad:
    nota = float(input('Nota '+str(i+1)+' : '))
    if nota >= 1 and nota <= 7:
        suma = suma + nota
        i = i + 1
    else:
        print('Nota NO valida, por favor reingrese nota')
promedio = suma / cantidad
print('Promedio: ', promedio)
if promedio >= 4:
    print('Se salvo')
else:
    print('R.I.P.')

