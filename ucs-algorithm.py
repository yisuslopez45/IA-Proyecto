def uniform_cost_search(graph, start, goal):
    # Guarda el menor costo conocido, empieza con el nodo inicical en 0
    dist = {start: 0}

    # Guarda el nodo de donde vienes, para reconstruir el camino
    # Ej: parent['B'] = 'A' significa que llegaste a B desde A.
    parent = {start: None}

    # Es la frontera, nodos por explorar, cada elemento es (costo, nodo)
    frontier = [(0, start)] 
    
    # Se ejecuta mientras haya nodos por explorar
    while frontier:

        # Ordena por el costo, lambda x: x[0] -> toma el costo del nodo
        frontier.sort(key=lambda x: x[0])

        # Saca el nodo con el menor costo, luego se elimina de la lista,
        # este siempre va estar en la primera posicion
        cost, node = frontier.pop(0)

        # Si ya existe una version mejor(menor costo) de este nodo, se ignora. 
        # float('inf'): infinito si el nodo no existe, de lo contrario el valor va -
        # ser el que tenga asociado el nodo.
        if cost > dist.get(node, float('inf')):
            continue

        # Si llegamos al objetivo
        if node == goal:
            # reconstruir camino
            path = []
            cur = goal
            while cur is not None:
                # print("Cur=",cur)
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path, cost
        # expandir vecinos
        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                parent[neighbor] = node
                frontier.append((new_cost, neighbor))
    return None, None
graph = {
    0.0: [(0.1, 4)],
    0.1: [(0.0, 2), (1.1,3) , (0.2, 6)],
    0.2: [(0.3, 4) , (0.1, 2)],
    0.3: [(0.4, 1) , (0.2, 2)],
    0.4: [(0.3, 2), (1.4, 2)],
    1.4: [(2.4, 4) , (0.4, 3)],
    2.4: [(2.3, 1) , (1.4, 5)],
    2.3: [(3.3, 8) , (2.2, 2) , (2.4, 4)],
    2.2: [(2.1, 2) , (2.3, 3)],
    2.1: [(1.1, 3) , (2.0, 1) , (2.2, 10)],
    1.1: [(0.1, 3) , (2.1, 1)],
    2.0: [(2.1, 2), (3.0, 2)],
    3.0: [(4.0, 1) , (2.0, 3)],
    4.0: [(3.0, 4) , (4.1, 3)],
    4.1: [(4.2, 1) , (4.0, 2)],
    4.2: [(4.3, 3) , (4.1, 1)],
    4.3: [(3.3, 1) , (4.2, 2) , (4.4, 3)],
    4.4: [(4.3, 2)],
    3.3: [(2.3, 3) , (4.3, 4)]
}




# Ejemplo: buscar de S a X
path, cost = uniform_cost_search(graph, 0.0, 4.4)
print("Camino óptimo:", path)
print("Costo total:", cost)