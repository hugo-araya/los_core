# Entero cap_invertir
# Real ganancia
cap_invertir = int(input('Capital a invertir: '))
porcentaje = float(input('Porcentaje: '))
meses = int(input('Meses: '))
ganancia = cap_invertir * (1 + porcentaje/100)**meses
print ('La ganancia es : ', ganancia, 'para un porcentaje del ', porcentaje,'%')
