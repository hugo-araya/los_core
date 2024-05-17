ent = open('terremotos.txt')
sal = open('terr.txt', 'w')
for linea in ent:
    lista = linea.split()
    lista = lista[:5]
    print(lista)
    sal.write(lista[0]+' '+lista[1]+' '+lista[2]+' '+lista[3]+' '+lista[4]+ '\n')
ent.close()
sal.close()

