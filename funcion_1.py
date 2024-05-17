import mibib as yo

def f(x):
    fx = 2 * x + 1
    return fx

if __name__ == '__main__':
    yo.limpiar()
    yo.saludo()
    valor = f(f(3))
    print(valor)
    print(__name__)


