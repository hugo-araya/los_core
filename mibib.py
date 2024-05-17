import os

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def saludo():
    print('Buenas noches')

if __name__ == '__main__':
    print(__name__)
