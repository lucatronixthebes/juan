import random

filas = random.randint(1, 10)
columnas = random.randint(1, 10)
matriz = []
sumaTotaldelasFilas = []

for x in range(0, filas):
    lista = []
    suma = 0
    for y in range(0, columnas):
        n = random.randint(1, 10)
        lista.append(n)
        suma += n
    matriz.append(lista.copy())
    sumaTotaldelasFilas.append(suma)

for x in range(0, filas):
    for y in range(0, columnas):
        print(matriz[x][y], end = " + ")
    print("\b\b=", sumaTotaldelasFilas[x])



    
