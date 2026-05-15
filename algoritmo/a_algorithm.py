


def a_star(  graph , heuristica  , start, goal):
    '''
    Conjunto de nodos pendientes por explorar.
    Comienza únicamente con el nodo inicial.
    '''
    nodos_abiertos = {start}
    
    '''
    Guarda desde qué nodo llegaste a otro nodo.
    Se usa luego para reconstruir el camino final.
    '''
    procede_del_nodo = {}
    
    # Lista de nodos visitados en orden de exploración.
    visitados = []

    '''
    g(n) -> costo acumulado desde el inicio hasta cada nodo.
    Todos comienzan en infinito excepto el nodo inicial.
    '''
    costo_acumulado = {city: float("inf") for city in graph}
    costo_acumulado[start] = 0

    '''
    f(n) = g(n) + h(n)
    g(n): costo acumulado
    h(n): heurística estimada hasta el objetivo
    '''
    f = {city: float("inf") for city in graph}
    
    '''
    Para el nodo inicial:
    f(start) = 0 + heuristica[start]
    '''
    f[start] = heuristica[start]

    # El algoritmo continúa mientras existan nodos por explorar
    while nodos_abiertos:
        
        '''
        Selecciona el nodo con el menor valor f(n),
        es decir, el nodo aparentemente más prometedor.
        '''
        current = min(nodos_abiertos, key=lambda x: f[x])
        
        visitados.append(current)

        # Si llegamos al objetivo
        if current == goal:
            
            '''
            Reconstrucción del camino desde el objetivo
            hasta el nodo inicial usando los padres.
            '''
            path = []
            while current in procede_del_nodo:
                path.append(current)
                current = procede_del_nodo[current]

            # Agrega el nodo inicial
            path.append(start)
            
            #Se invierte porque el camino se construyó al revés
            return path[::-1], costo_acumulado[goal] , visitados
        
        '''
        El nodo actual deja de estar pendiente
        porque ya fue explorado.
        '''
        nodos_abiertos.remove(current)
        
        # Recorre todos los vecinos del nodo actual
        for vecino, cost in graph[current].items():
            ''' 
            Calcula el nuevo costo acumulado
            para llegar al vecino pasando por current.
            '''
            tentative_g = costo_acumulado[current] + cost
            ''' 
            Si encontramos un camino más barato
            hacia el vecino, actualizamos la información.
            ''' 
            if tentative_g < costo_acumulado[vecino]:
                
                #Guarda desde dónde llegamos al vecino
                procede_del_nodo[vecino] = current
                
                #Actualiza el costo acumulado real
                costo_acumulado[vecino] = tentative_g
                
                '''
                f(n) = g(n) + h(n)
                Combina:
                    - costo real recorrido
                    - estimación  heuristica al objetivo
                '''
                f[vecino] = tentative_g + heuristica[vecino]
                
                
                #Agrega el vecino a los nodos pendientes
                nodos_abiertos.add(vecino)
                
    return None, float("inf")


