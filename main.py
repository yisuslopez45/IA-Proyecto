#Construyen el grafo partiendo de una matriz
from map.map_grafo_simple import map_grafo as map_grafo_simple
from map.map_grafo_ucs import map_grafo as map_grafo_ucs
from map.map_heuristica import calc_heuristica

#Algoritmos de busqueda
from algoritmo.profundidad_algorithm import dfs_camino as bfs_camino_profundidad
from algoritmo.amplitud_algorithm import bfs_camino as bfs_camino_amplitud
from algoritmo.ucs_algorithm import uniform_cost_search as ucs_camino



from menu import mostrar_menu

laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
]

inicio = 0.0
objetivo = 4.4

grafo = map_grafo_simple(laberinto)
grafo_ucs = map_grafo_ucs(laberinto)
heuristica = calc_heuristica( matriz = laberinto , objetivo = objetivo )



# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        camino, visitados, predecesores = bfs_camino_profundidad( grafo=grafo, inicio= inicio , objetivo= objetivo)
        print(camino)
    
    elif opcion == "2":
        camino = bfs_camino_amplitud( grafo=grafo  , inicio = inicio , objetivo = objetivo)
        print(camino)
        
    elif opcion == "3":
        path, cost = ucs_camino(graph=grafo_ucs , start=inicio , goal=objetivo)
        print(path)
        print(cost)
        
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")


