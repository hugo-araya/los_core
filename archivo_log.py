import bib_log

ARCHIVO_LOG = "mi_log.txt"

if __name__ == "__main__":
    archivo_log = bib_log.abrir_log(ARCHIVO_LOG)
    error = True
    if error:
        bib_log.guardar_log(archivo_log, "ERROR: "+str(error))
    bib_log.cerrar_log(archivo_log)