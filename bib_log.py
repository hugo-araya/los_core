# Código: bib_log.py: Módulo para manipulación de archivos de log

import datetime

def abrir_log(nombre_log):
    archivo_log = open(nombre_log, "a")
    guardar_log(archivo_log, "Iniciando registro de errores")
    return archivo_log

def guardar_log(archivo_log, mensaje):
    hora_actual = str(datetime.datetime.now())
    archivo_log.write(hora_actual+" "+mensaje+"\n")

def cerrar_log(archivo_log):
    guardar_log(archivo_log, "Fin del registro de errores")
    archivo_log.close()
