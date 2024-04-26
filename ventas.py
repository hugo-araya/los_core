# indicar el tipo de datos de cada variable 
sueldo_base = int(input('Sueldo: '))
venta1 = int(input())
venta2 = int(input())
venta3 = int(input())
total_venta = venta1 + venta2 + venta3 
comision = total_venta * 0.10 
sueldo_recibir = sueldo_base + comision 
print ('Comision: ', comision)
print ('Sueldo a recibir: ', sueldo_recibir)