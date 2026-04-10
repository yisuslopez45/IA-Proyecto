

# graph = {
#     0.0: {1.0: 2},
#     0.2: {0.3: 1, 1.2: 4},
#     0.3: {0.4: 3, 0.2: 8},
#     0.4: {0.3: 4, 1.4: 4},
#     1.0: {1.1: 6, 2.0: 2, 0.0: 5},
#     1.1: {1.2: 8, 1.0: 3},
#     1.2: {1.1: 1, 2.2: 3, 0.2: 2},
#     1.4: {2.4: 2, 0.4: 2},
#     2.0: {3.0: 6, 1.0: 3},
#     2.2: {3.2: 6, 1.2: 7},
#     2.4: {3.4: 9, 1.4: 3},
#     3.0: {4.0: 3, 2.0: 5},
#     3.2: {3.3: 4, 4.2: 4, 2.2: 2},
#     3.3: {3.4: 6, 3.2: 3},
#     3.4: {3.3: 7, 4.4: 8, 2.4: 4},
#     4.0: {4.1: 6, 3.0: 2},
#     4.1: {4.2: 2, 4.0: 4},
#     4.2: {4.1: 8, 3.2: 1},
#     4.4: {3.4: 1},
# }

# h = {
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



def a_star(  graph , heuristica  , start, goal):
    nodos_abiertos = {start}
    procede_del_nodo = {}

    costo_acumulado = {city: float("inf") for city in graph}
    costo_acumulado[start] = 0

    f = {city: float("inf") for city in graph}
    f[start] = heuristica[start]

    while nodos_abiertos:
        current = min(nodos_abiertos, key=lambda x: f[x])
        # print("#### CURRENT ####", current)
        # print("\n")
        if current == goal:
            path = []
            while current in procede_del_nodo:
                path.append(current)
                current = procede_del_nodo[current]
            path.append(start)
            return path[::-1], costo_acumulado[goal]
        
        nodos_abiertos.remove(current)
        
        for vecino, cost in graph[current].items():
 
            tentative_g = costo_acumulado[current] + cost
            if tentative_g < costo_acumulado[vecino]:
                procede_del_nodo[vecino] = current
                costo_acumulado[vecino] = tentative_g
                f[vecino] = tentative_g + heuristica[vecino]
                nodos_abiertos.add(vecino)
                
    return None, float("inf")


# camino, costo_acumulado = a_star(0.0, 4.4)
# print("Camino:", camino)
# print("Costo_acumulado:", costo_acumulado)
