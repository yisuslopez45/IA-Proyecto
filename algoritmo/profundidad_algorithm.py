def dfs_camino(grafo, inicio, objetivo):
    # Estructuras necesarias
    pila = [inicio]              # pila para DFS
    visitados = set()            # conjunto de nodos visitados
    predecesores = {inicio: None}  # diccionario de predecesores
    while pila:

        nodo = pila.pop()  # se saca el último

        if nodo not in visitados:
            visitados.add(nodo)
            # Si llegamos al objetivo, reconstruimos el camino
            if nodo == objetivo:
                camino = []
                actual = nodo
                while actual is not None:
                    camino.append(actual)
                    actual = predecesores[actual]
                camino.reverse()
                return camino, visitados, predecesores
            # Agregar vecinos a la pila
            vecinos = grafo[nodo]
            for vecino in reversed(vecinos):  # invertir orden
                if vecino not in predecesores:
                    predecesores[vecino] = nodo
                    pila.append(vecino)
    return None, visitados, predecesores
