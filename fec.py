ter = "08/02/1570 9:00 -36.800 -73.000 8.3"
l = ter.split()
print(l)
fecha = l[0].split('/')
print(fecha[1])
if fecha[1] == '02':
    print('Febrero')
else:
    print('Otro mes')
    