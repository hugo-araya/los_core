cap_inv = int(input('Capital: '))
p_interes = float(input('Interes: '))
saldo = cap_inv
interes_calculado = cap_inv * p_interes /100
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
print ('Saldo: ', saldo)
