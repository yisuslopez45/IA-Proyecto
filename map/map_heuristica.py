# laberinto = [
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
# ]


def calc_heuristica(matriz, objetivo):
    grafo = {}
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[j][i] == 1:
                nodo = float(f"{j}.{i}")
                x_objectivo, y_objetivo = str(objetivo).split(".")

                x_objectivo = int(x_objectivo)
                y_objetivo = int(y_objetivo)

                h_manhattan = (-1) * (j - x_objectivo) + (-1) * (i - y_objetivo)
                grafo[nodo] = h_manhattan
    return grafo


# print(calc_heuristica(laberinto, 4.4))
# print(map_grafo(laberinto))

# ff = {
#     0.0: 8,
#     1.0: 7,
#     2.0: 6,
#     3.0: 5,
#     4.0: 4,
#     1.1: 6,
#     4.1: 3,
#     0.2: 6,
#     1.2: 5,
#     2.2: 4,
#     3.2: 3,
#     4.2: 2,
#     0.3: 5,
#     3.3: 2,
#     0.4: 4,
#     1.4: 3,
#     2.4: 2,
#     3.4: 1,
#     4.4: 0,
# }
