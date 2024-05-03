# Real Nota1, Nota2, Nota3, Nota4, Nota5, Nota6, Nota7 
# Real Promedio
contador = 0
suma = 0
cantidad = int(input('Cantidad de notas: '))
while contador < cantidad:
    nota = float(input('Nota '+str(contador+1)+': '))
    suma = suma + nota
    contador = contador + 1
promedio = suma / cantidad
print('Promedio: ', promedio)
if promedio >= 4:
    if promedio >= 5:
        print('Estudiastes')
    else:
        print('Dios es grande, te salvastes')
else:
    print('R.I.P')
