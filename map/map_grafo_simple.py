# laberinto = [
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
# ]


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


# print(map_grafo(laberinto))


# test = {
#     0.0: [1.0],
#     1.0: [1.1, 0.0, 2.0],
#     2.0: [1.0, 3.0],
#     3.0: [2.0, 4.0],
#     4.0: [4.1, 3.0],
#     1.1: [(1.0, 6), 1.2],
#     4.1: [(4.0, 6), 4.2],
#     0.2: [0.3, 1.2],
#     1.2: [(1.1, 6), 0.2, 2.2],
#     2.2: [1.2, 3.2],
#     3.2: [3.3, 2.2, 4.2],
#     4.2: [(4.1, 6), 3.2],
#     0.3: [(0.2, 6), 0.4],
#     3.3: [(3.2, 6), 3.4],
#     0.4: [(0.3, 6), 1.4],
#     1.4: [0.4, 2.4],
#     2.4: [1.4, 3.4],
#     3.4: [(3.3, 6), 2.4, 4.4],
#     4.4: [3.4],
# }
