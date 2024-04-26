# 55% del promedio de sus tres notas parciales. 
# 30% de la nota del examen final.
# 15% de la nota de un trabajo final.

# Lectura
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
ex_final = float(input('Examen Final: '))
tr_final = float(input('Trabajo final: '))
# Calculos
notas = (nota1+ nota2+ nota3)/3
nota_final = notas * 0.55 + ex_final * 0.3 + tr_final * 0.15
# Salida
print('La nota final es: ', nota_final)
