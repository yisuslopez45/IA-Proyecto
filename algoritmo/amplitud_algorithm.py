

def bfs_camino(grafo, inicio, objetivo):
    cola = [inicio]                 # usamos lista en lugar de deque
    visitados = {inicio}
    predecesor = {inicio: None}

    while cola:
        nodo = cola.pop(0)          # sacamos el primer elemento (FIFO)
        
        if nodo == objetivo:
            # reconstrucción del camino
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = predecesor[nodo]
            return list(reversed(camino)) ,  visitados
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                predecesor[vecino] = nodo
                cola.append(vecino) # encolamos al final

    return None  # si no se encuentra camino

# Definimos el grafo
# grafo = {
#     0.0: [0.1],
#     0.1: [0.2, 1.1 , 0.0],
#     0.2: [0.3 , 0.1],
#     0.3: [0.4 , 0.2],
#     0.4: [0.3, 1.4],
#     1.4: [2.4 , 0.4],
#     2.4: [2.3 , 1.4],
#     2.3: [3.3 , 2.2 , 2.4],
#     2.2: [2.1 , 2.3],
#     2.1: [1.1 , 2.0 , 2.2],
#     1.1: [0.1 , 2.1],
#     2.0: [2.1, 3.0],
#     3.0: [4.0 , 2.0],
#     4.0: [3.0 , 4.1],
#     4.1: [4.2 , 4.0],
#     4.2: [4.3 , 4.1],
#     4.3: [3.3 , 4.2 , 4.4],
#     4.4: [],
#     3.3: [2.3 , 4.3]
# }

# camino = bfs_camino(grafo, 0.0, 4.4)
# print("Camino más corto:", camino)

