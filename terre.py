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

def funcion_a(datos):
    mayor = -1
    fecha = ''
    hora = ''
    for lista in datos:
        if float(lista[4]) > mayor:
            mayor = float(lista[4])
            fecha = lista[0]
            hora = lista[1]
    return [fecha, hora, mayor]

def funcion_b(datos):
    suma = 0
    for lista in datos:
        if float(lista[4]) >= 7 and float(lista[4]) < 8:
            suma = suma + 1
    return suma

def funcion_c(datos):
    suma = 0
    for lista in datos:
        if float(lista[4]) >= 8 and float(lista[4]) < 9:
            suma = suma + 1
    return suma

def funcion_d(datos):
    suma = 0
    for lista in datos:
        if float(lista[4]) > 9:
            suma = suma + 1
    return suma

def funcion_e(datos):
    suma = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) < 1600:
            suma = suma + 1
    return suma

def funcion_f(datos):
    suma = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) >= 1600 and float(fecha[2]) < 1700:
            suma = suma + 1
    return suma

def funcion_g(datos):
    suma = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) >= 1700 and float(fecha[2]) < 1800:
            suma = suma + 1
    return suma

def funcion_h(datos):
    suma = 0
    for lista in datos:
        fecha = lista[0]
        fecha = fecha.split('/')
        if float(fecha[2]) >= 1800 and float(fecha[2]) < 1900:
            suma = suma + 1
    return suma

def muestra_datos(sismo_mayor, sismos_7_8, sismos_8_9, sismos_9, sismo_16, sismo_17, sismo_18, sismo_19):
    print(sismo_mayor)
    print(sismos_7_8)
    print(sismos_8_9)
    print(sismos_9)
    print(sismo_16)
    print(sismo_17)
    print(sismo_18)
    print(sismo_19)

def grafica(y):
    x = [16, 17, 18, 19]
    plt.pie(y)
    plt.show()

if __name__ == '__main__':
    datos = lee_datos('terr.txt')
    sismo_mayor = funcion_a(datos)
    sismos_7_8 = funcion_b(datos)
    sismos_8_9 = funcion_c(datos)
    sismos_9 = funcion_d(datos)
    sismo_16 = funcion_e(datos)
    sismo_17 = funcion_f(datos)
    sismo_18 = funcion_g(datos)
    sismo_19 = funcion_h(datos)
    muestra_datos(sismo_mayor, sismos_7_8, sismos_8_9, sismos_9, sismo_16, sismo_17, sismo_18, sismo_19)
    grafica([sismo_16, sismo_17, sismo_18, sismo_19])