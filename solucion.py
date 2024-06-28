import matplotlib.pyplot as plt

def lectura_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    ent.close()
    return datos        

def region_todas(datos):
    regiones = []
    for dato in datos:
        if dato[2] not in regiones:
            regiones.append(dato[2])
    return regiones

def funcion_a(datos):
    regiones = region_todas(datos)
    casos = []
    for region in regiones:
        cont = 0
        for dato in datos:
            if region == dato[2]:
                cont = cont + int(dato[7])
        casos.append([region, cont])
    return casos

def funcion_b(datos):
    cont = 0
    for dato in datos:
        fecha = dato[0].split('-')
        if fecha[1] == '01' and fecha[2] == '2023':
            cont = cont + int(dato[7])
    return cont

def funcion_c(datos):
    cont = 0
    for dato in datos:
        if 'Tagua' in dato[6] and dato[3] == 'Cartagena':
            cont = cont + int(dato[7])
    return cont   

def funcion_d(datos):
    cont = 0
    for dato in datos:
        fecha = dato[0].split('-')
        if fecha[0] == '12' and fecha[1] == '02' and fecha[2] == '2023' and ('Piquero' in dato[6]):
            cont = cont + int(dato[7])
    return cont    

def funcion_e(datos):
    cont_garuma = 0
    cont_piquero = 0
    cont_franklin = 0
    cont_pelicano = 0
    cont_guanay = 0
    for dato in datos:
        if 'Gaviota garuma' in dato[6]:
            cont_garuma = cont_garuma + 1
        if 'Piquero' in dato[6]:
            cont_piquero = cont_piquero + 1
        if 'Gaviota de Franklin' in dato[6]:
            cont_franklin = cont_franklin + 1
        if 'Pelicano' in dato[6]:
            cont_pelicano = cont_pelicano + 1
        if 'Guanay' in dato[6]:
            cont_guanay = cont_guanay + 1
    especies = ['G. Garuma', 'Piquero', 'G. Franklin', 'Pelicano', 'Guanay']
    salida = [cont_garuma, cont_piquero, cont_franklin, cont_pelicano, cont_guanay]
    plt.bar(especies, salida)
    plt.show()

def genera_salida(res_a, res_b, res_c, res_d):
    sal = open('resultado.txt', 'w')
    sal.write('Autor(es): nnnnnnnn - nnnnnnnn\n\n')
    sal.write('Cantidad de aves muertas por region:\n\n')
    for dato in res_a:
        sal.write('\t'+dato[0]+': '+str(dato[1])+'\n\n')
    
    sal.write('Casos aves muertas mes enero del año 2023: '+str(res_b)+'\n\n')
    sal.write('En la comuna de Cartagena se detectaron '+str(res_c)+' Taguas muertas\n\n')
    sal.write('Las muertes detectadas para el 12 de febrero 2023 de la especie Piquero son: '+str(res_d)+'\n\n')
    sal.close()

if __name__ == '__main__':
    datos = lectura_datos('aves.txt')
    res_a = funcion_a(datos)
    res_b = funcion_b(datos)
    res_c = funcion_c(datos)
    res_d = funcion_d(datos)
    funcion_e(datos)
    genera_salida(res_a, res_b, res_c, res_d)









