# Autor: Hugo Araya Carrasco
# Fecha: 07/08/2024
# Version : 0.0

def lectura(nombre):
    ent = open(nombre)
    linea1 = ent.readline().rstrip('\n')
    linea2 = ent.readline().rstrip('\n')
    return linea1, linea2

def lee_coaliciones(coaliciones):
    coalicion = []
    aux = coaliciones.split(';')
    for elem in aux:
        paso = elem.split(':')
        coalicion.append(paso)
    return coalicion

def genera_partidos(coalicion):
    partidos = []
    for elem in coalicion:
        part = elem[1].split('-')
        for p in part:
            partidos.append([p, 0])
    return partidos

def genera_votos(votacion):
    votos = votacion.split('$')
    return votos

def suma_votos(partidos, votos):
    for voto in votos:
        for elem in partidos:
            if voto == elem[0]: 
                elem[1] = elem[1] + 1
    return partidos

if __name__ == '__main__':
    coaliciones, votacion = lectura('elecciones.txt')
    coalicion = lee_coaliciones(coaliciones)
    partidos = genera_partidos(coalicion)
    votos = genera_votos(votacion)
    partidos = suma_votos(partidos, votos)
    print(partidos)




