def dfs_camino(grafo, inicio, objetivo):
    # Estructuras necesarias
    pila = [inicio]              # pila para DFS
    visitados = set()            # conjunto de nodos visitados
    predecesores = {inicio: None}  # diccionario de predecesores
    while pila:
        print("-----------------------------------------------------")
        # print("pila",pila)
        nodo = pila.pop()  # se saca el último
        # print("nodo analizado=",nodo)
        # print("Visitados=",visitados)
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
            # print("Vecinos=",vecinos)
            for vecino in reversed(vecinos):  # invertir orden
                if vecino not in predecesores:
                    predecesores[vecino] = nodo
                    pila.append(vecino)
            # print("Predecesores=",predecesores)
    return None, visitados, predecesores


# Definición del grafo (lista de adyacencia)
# grafo = {
#     0.0: [0.1],
#     0.1: [0.0, 1.1 , 0.2],
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


# Ejecutar DFS
# camino, visitados, predecesores = dfs_camino(grafo, 0.0, 4.4)

# print("Camino encontrado:", camino)
# print("Visitados:", visitados)
# print("Predecesores:", predecesores)