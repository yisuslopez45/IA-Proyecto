# Grafo con costos reales (distancias)
graph = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucarest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucarest": 101},
    "Bucarest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucarest": 90},
    "Urziceni": {"Bucarest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
}

# Heurística h(n): distancia en línea recta a Bucarest
h = {
    "Arad": 366,
    "Bucarest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}


def a_star(start, goal):
    nodos_abiertos = {start}
    procede_del_nodo = {}

    g = {city: float("inf") for city in graph}
    #  {
    #     "Arad": inf,
    #     ...
    #  }

    g[start] = 0
    

    f = {city: float("inf") for city in graph}
    #  {
    #     "Arad": inf,
    #     ...
    #  }

    # f = se llena con la heuristica
    f[start] = h[start]
    
    print('nodos abiertos', nodos_abiertos)


    while nodos_abiertos:
        # nodo con menor f
        current = min(nodos_abiertos, key=lambda x: f[x])
        # print('current', current)
        if current == goal:
            # reconstruir camino
            path = []
            while current in procede_del_nodo:
                path.append(current)
                current = procede_del_nodo[current]
            path.append(start)
            return path[::-1], g[goal]

        nodos_abiertos.remove(current)
        for vecino, cost in graph[current].items():
            # SACA LOS ITEMS DEL CURRENT
            print('items', graph[current].items())
       
            tentative_g = g[current] + cost
            print('tentative ', tentative_g)
            if tentative_g < g[vecino]:
                procede_del_nodo[vecino] = current
                g[vecino] = tentative_g
                f[vecino] = tentative_g + h[vecino]
                nodos_abiertos.add(vecino)

    return None, float("inf")


camino, costo = a_star("Arad", "Bucarest")
# print("Camino:", camino)
# print("Costo:", costo)



# g: {
#     "Arad": 0,
#     "Zerind": inf,
#     "Oradea": inf,
#     "Sibiu": inf,
#     "Timisoara": inf,
#     "Lugoj": inf,
#     "Mehadia": inf,
#     "Dobreta": inf,
#     "Craiova": inf,
#     "Rimnicu Vilcea": inf,
#     "Fagaras": inf,
#     "Pitesti": inf,
#     "Bucarest": inf,
#     "Giurgiu": inf,
#     "Urziceni": inf,
#     "Hirsova": inf,
#     "Eforie": inf,
#     "Vaslui": inf,
#     "Iasi": inf,
#     "Neamt": inf,
# }
# f: {
#     "Arad": 366,
#     "Zerind": inf,
#     "Oradea": inf,
#     "Sibiu": inf,
#     "Timisoara": inf,
#     "Lugoj": inf,
#     "Mehadia": inf,
#     "Dobreta": inf,
#     "Craiova": inf,
#     "Rimnicu Vilcea": inf,
#     "Fagaras": inf,
#     "Pitesti": inf,
#     "Bucarest": inf,
#     "Giurgiu": inf,
#     "Urziceni": inf,
#     "Hirsova": inf,
#     "Eforie": inf,
#     "Vaslui": inf,
#     "Iasi": inf,
#     "Neamt": inf,
# }
