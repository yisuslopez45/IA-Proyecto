#Construyen el grafo partiendo de una matriz
from map.map_grafo_simple import map_grafo as map_grafo_simple
from map.map_grafo_ucs import map_grafo as map_grafo_ucs
from map.map_heuristica import calc_heuristica
from map.map_grafo_start import map_grafo as map_grafo_estrella

#Algoritmos de busqueda
from algoritmo.profundidad_algorithm import dfs_camino as bfs_camino_profundidad
from algoritmo.amplitud_algorithm import bfs_camino as bfs_camino_amplitud
from algoritmo.ucs_algorithm import uniform_cost_search as ucs_camino
from algoritmo.a_algorithm import a_star as a_estrella_camino
from laberinto.generar_laberinto import randomLaberinto , imprimirSolucion , imprimirLaberinto , addCostosLaberinto




from menu import mostrar_menu

# laberinto = [
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
# ]
laberinto_simple = randomLaberinto()
laberinto_costos = addCostosLaberinto(laberinto_simple)

inicio = "0.0"
objetivo = "26.26"

grafo = map_grafo_simple(laberinto_simple)
grafo_ucs = map_grafo_ucs(laberinto_costos)
grafo_estrella = map_grafo_estrella(laberinto_costos)
heuristica = calc_heuristica( matriz = laberinto_simple , objetivo = objetivo )

print("\n")
print("Laberinto Generado Aleatoriamente")
print("#################################################################################\n")

# imprimirLaberinto(laberinto_simple)
imprimirLaberinto(laberinto_costos)

print("#################################################################################")
print('\n')

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        camino, visitados, predecesores = bfs_camino_profundidad( grafo=grafo, inicio= inicio , objetivo= objetivo)
        imprimirSolucion(laberinto_simple,camino)
    
    elif opcion == "2":
        camino = bfs_camino_amplitud( grafo=grafo  , inicio = inicio , objetivo = objetivo)
        imprimirSolucion(laberinto_simple,camino)
        # print(camino)
        
    elif opcion == "3":
        path, cost = ucs_camino(graph=grafo_ucs , start=inicio , goal=objetivo)
        imprimirSolucion(laberinto_simple,path)
        
    elif opcion == "4":
        camino, costo_acumulado = a_estrella_camino( graph= grafo_estrella , heuristica = heuristica , start=inicio , goal=objetivo)
        imprimirSolucion(laberinto_simple,camino)
        # print("Camino:", camino)
        # print("Costo_acumulado:", costo_acumulado)
        
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")


