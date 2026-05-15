"""
Funcion encargada de generar el grafo a partir de una matriz, -
en donde la key es el nodo 'i,j' y el value son los vecinos a donde 
se puede mover, se analiza cada posicion.

Grafo de ejemplo
{
    '0.0': ['1.0'],
    '1.0': ['1.1', '0.0', '2.0'],
    ...
}
"""
def map_grafo(matriz):
    grafo = {}
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[j][i] == 1:
                vecinos = []
                nodo = f"{j}.{i}"
                # ARRIBA
                if i - 1 >= 0 and matriz[j][i - 1] != 0:
                    vecinos.append(f"{j}.{i-1}")
                # ABAJO
                if i + 1 < columnas and matriz[j][i + 1] != 0:
                    vecinos.append(f"{j}.{i+1}")
                # IZQUIERDA
                if j - 1 >= 0 and matriz[j - 1][i] != 0:
                    vecinos.append(f"{j-1}.{i}")
                # DERECHA
                if j + 1 < filas and matriz[j + 1][i] != 0:
                    vecinos.append(f"{j+1}.{i}")

                grafo[nodo] = vecinos
    return grafo
