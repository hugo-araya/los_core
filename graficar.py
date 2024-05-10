import matplotlib.pyplot as plt
#Importa el módulo pyplot y genera el alias plt
X = []
Y = []
i = -4
while i <= 4.1:
    X.append(i)
    Y.append(i*i)
    i = i + 0.01
plt.plot(X,Y)
plt.title('Grafico de ejemplo')
plt.show()
