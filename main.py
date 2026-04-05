from map_grafo_simple import map_grafo
from profundidad import dfs_camino
from amplitud import bfs_camino_amplitud
from menu import mostrar_menu

laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
]


grafo = map_grafo(laberinto)



# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        camino, visitados, predecesores = dfs_camino( grafo=grafo, inicio= 0.0 , objetivo= 4.4)
        print(camino)
    
    elif opcion == "2":
        camino = bfs_camino_amplitud( grafo=grafo  , inicio = 0.0 , objetivo = 4.4)
        print(camino)
        
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")


