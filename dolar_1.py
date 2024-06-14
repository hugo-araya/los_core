# Autor(es) : Hugo Araya Carrasco
import matplotlib.pyplot as plt

def lee_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos

def calcula_promedios(datos):
    year = 2013
    promedios = []
    while year < 2020:
        suma = 0
        cantidad = 0
        for dato in datos:
            fecha = dato[0].split('-')
            if int(fecha[2]) == year:
                suma = suma + float(dato[1])
                cantidad = cantidad + 1
        promedio = suma / cantidad
        promedios.append([year, promedio])
        year = year + 1
    return promedios

def determina_minimo(datos):
    mini = 2000
    for dato in datos:
        if float(dato[1]) < mini:
            mini = float(dato[1])
            fecha = dato[0]
    return [fecha, mini]

def determina_maximo(datos):
    maxi = 0
    for dato in datos:
        if float(dato[1]) > maxi:
            maxi = float(dato[1])
            fecha = dato[0]
    return [fecha, maxi]

def genera_salida(promedios, minimo, maximo):
    sal = open('resumen.txt', 'w')
    for promedio in promedios:
        sal.write('Promedio '+ str(promedio[0]) + ' : ' + str(promedio[1]) + '\n\n')
    fecha = maximo[0].split('-')
    sal.write('El mayor valor corresponde al dia '+fecha[0]+ ' del mes '+fecha[1]+' de '+fecha[2]+'\n\n')
    fecha = minimo[0].split('-')
    sal.write('El menor valor corresponde al dia '+fecha[0]+ ' del mes '+fecha[1]+' de '+fecha[2]+'\n\n')
    sal.close()

def grafica(promedios):
    x = []
    y = []
    for promedio in promedios:
        x.append(promedio[0])
        y.append(promedio[1])
    plt.bar(x, y)
    plt.show()

if __name__ == '__main__':
    datos = lee_datos('datos.txt')
    promedios = calcula_promedios(datos)
    minimo = determina_minimo(datos)
    maximo = determina_maximo(datos)
    genera_salida(promedios, minimo, maximo)
    grafica(promedios)

