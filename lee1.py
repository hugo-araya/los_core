ent = open('nosetxt.txt')
suma = 0
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split()
    suma = suma + int(lista[1])
print(suma)
