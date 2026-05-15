

def bfs_camino(grafo, inicio, objetivo):
    cola = [inicio]   # usamos lista en lugar de deque
    visitados = {inicio}
    predecesor = {inicio: None}

    while cola:
        nodo = cola.pop(0)    # sacamos el primer elemento (FIFO)
        
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

    return None

