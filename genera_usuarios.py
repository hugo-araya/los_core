def lectura_datos(archivo):
    ent = open(archivo)
    nombres = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        nombres.append(lista)
    ent.close()
    return nombres

def generador_usuarios(nombres):
    usuarios = []
    for nombre in nombres:
        login = nombre[0][0] + nombre[1]
        login = login.lower()
        if login in usuarios:
            login = login + nombre[2].upper()
        usuarios.append(login)
    return usuarios

def grabacion_usuarios(usuarios):
    salida = open('usuarios.txt', 'w')
    for usuario in usuarios:
        salida.write(usuario+'\n')
    salida.close()

if __name__ == '__main__':
    nombres = lectura_datos('nombres.txt')
    usuarios = generador_usuarios(nombres)
    grabacion_usuarios(usuarios)
