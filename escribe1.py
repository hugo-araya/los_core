ent = open('wnosetxt.txt')
sal = open('nuevo.txt', 'w')
for linea in ent:
    sal.write(linea)
ent.close()
sal.close()
