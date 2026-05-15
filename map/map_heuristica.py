"""
Funcion encargada de calcular la heuristica de manhattan, de acuerdo -
a la posiciones de la matriz
d = |x1 - x2| + |y1 - y2|
"""

def calc_heuristica(matriz, objetivo):
    grafo = {}
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[j][i] == 1:
                nodo = f"{j}.{i}"
                x_objectivo, y_objetivo = str(objetivo).split(".")

                x_objectivo = int(x_objectivo)
                y_objetivo = int(y_objetivo)

                h_manhattan = (-1) * (j - x_objectivo) + (-1) * (i - y_objetivo)
                grafo[nodo] = h_manhattan
    return grafo

