cap_inv = int(input('Capital: '))
p_interes = float(input('Interes: '))
interes_calculado = cap_inv * p_interes /100
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
else:
    saldo = cap_inv
salida = 'Para un capital de $'+str(cap_inv)+' y un interes de '+str(p_interes)+'% da un saldo de $'+str(saldo)

print (salida)
