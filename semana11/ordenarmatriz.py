#ALGORITMO DE ORDENACION
#CREAMOS UNA MATRIZ BIDIMENSIONAL 3X3
matriz=[[40,50,60],
        [15,20,13],
        [90,50,80]]

print(f"MATRIZ ORIGINAL")
#UTILIZAMOS FOR PARA IMPRIMIR LA MATRIZ ORIGINAL
for x in matriz:
        print(x)
# QUEREMOS ORDENAR LA SEGUNDA FILA
fila=1 # EN LA MATRIZ SE ENCUENTRA EN LA FILA 1
# USAMOS UN ALGORITMO DE ORDENACION SORT
matriz[fila].sort()
#IMPRIMIMOS LA SEGUNDA FILA EN ORDEN ASCENDENTE
print(f"ORDENAR SEGUNDA FILA EN ORDEN ASCENDENTE")
print(matriz[fila])