
'''
Construyen el grafo partiendo de una matriz
Se realizan las importaciones de las funciones que mapean la matriz del laberinto 
y retornan un grafo
'''
from map.map_grafo_simple import map_grafo as map_grafo_simple
from map.map_grafo_ucs import map_grafo as map_grafo_ucs
from map.map_heuristica import calc_heuristica
from map.map_grafo_start import map_grafo as map_grafo_estrella

'''
Se realizan las importaciones de los algoritmos de busqueda
'''
from algoritmo.profundidad_algorithm import dfs_camino as bfs_camino_profundidad
from algoritmo.amplitud_algorithm import bfs_camino as bfs_camino_amplitud
from algoritmo.ucs_algorithm import uniform_cost_search as ucs_camino
from algoritmo.a_algorithm import a_star as a_estrella_camino

'''
Desde la carpeta laberinto de importan 3 funciones que se utilizan sobre el laberinto
    - imprimirSolucion (Imprime la solucion en consola)
    - imprimirLaberinto (Unicamente imprime el laberinto solo, sin solucion)
    - addCostosLaberinto (La utilizamos para cargar el laberinto para el algoritmo de UCS Y A* )

Se importa el laberinto que es una matriz de 90*90
'''
from laberinto.acciones_laberinto import  imprimirSolucion , imprimirLaberinto , addCostosLaberinto
from laberinto.laberinto import laberinto as laberinto_simple

'''
Desde la carpeta Utils  se importan 2 funciones
    - generar_imagen_laberinto (Genera una img .png del laberinto y la guarda local)
    - generar_imagen_con_solucion (Generad una img .png para visualizar el laberinto con sus respectivos pesos)
    - limpiar_imagenes_soluciones (elimina todas las .png del local)
'''
from utils.generar_img import generar_imagen_laberinto , generar_imagen_con_solucion
from utils.eliminar_img import limpiar_imagenes_soluciones

import time


from menu import mostrar_menu

# Elimina imágenes viejas antes de comenzar
limpiar_imagenes_soluciones()

# Agrega costos al laberinto para UCS y A*
laberinto_costos = addCostosLaberinto(laberinto_simple)


# Nodo inicial y nodo objetivo
inicio = "0.0"
objetivo = "90.90"

# Guarda estadísticas y resultados de cada algoritmo
resumen = {}

# Guarda tiempos de ejecución para calcular promedios
tiempo = {
    "1" : [],
    "2" : [],
    "3" : [],
    "4" : []
}

# Construcción de grafos para cada algoritmo
grafo = map_grafo_simple(laberinto_simple)
grafo_ucs = map_grafo_ucs(laberinto_costos)
grafo_estrella = map_grafo_estrella(laberinto_costos)

# Calcula la heurística usada por A*
heuristica = calc_heuristica( matriz = laberinto_simple , objetivo = objetivo )

print("\n")
print("Laberinto Generado Aleatoriamente")
print("#################################################################################\n")

imprimirLaberinto(laberinto_costos)
generar_imagen_laberinto(laberinto_costos , escala=20 , output= "img_soluciones/inicial.png")

print("#################################################################################")
print('\n')

# ==========================
# Programa principal
# ==========================

while True:
    
    # Muestra el menú y estadísticas
    mostrar_menu(resumen)
    opcion = input("Selecciona una opción: ")

    # =========================================
    # DFS - Búsqueda en profundidad
    # =========================================
    if opcion == "1":
        t_inicio = time.time()
        camino, visitados, predecesores = bfs_camino_profundidad( grafo=grafo, inicio= inicio , objetivo= objetivo)
        f_inicio = time.time()
        
        # Guarda tiempo de ejecución
        tiempo["1"].append( f_inicio - t_inicio)
        suma_tiempo = tiempo['1']
        
        # Guarda estadísticas
        resumen["1"] = {
            "algoritmo" : "DFS PROFUNDIDAD",
            "tiempo" : f_inicio - t_inicio,
            "n_nodos_solucion" :  len(camino),
            "visitados" : len(visitados),
            "promedio_tiempo" : sum(suma_tiempo)/len(suma_tiempo),
            "numero_intentos" : len(suma_tiempo)
        }
        
        # Genera imagen y muestra solución
        generar_imagen_con_solucion(laberinto_simple,camino,escala=12, output= "img_soluciones/DFS_SOLUCION.png")   
        imprimirSolucion(laberinto_simple,camino)
    
    # =========================================
    # BFS - Búsqueda en amplitud
    # =========================================
    elif opcion == "2":
        t_inicio = time.time()
        camino , visitados  = bfs_camino_amplitud( grafo=grafo  , inicio = inicio , objetivo = objetivo)
        f_inicio = time.time()
        
        tiempo["2"].append( f_inicio - t_inicio)
        suma_tiempo = tiempo['2']

        resumen["2"] = {
            "algoritmo" : "BFS AMPLITUD",
            "tiempo" : f_inicio - t_inicio,
            "n_nodos_solucion" :  len(camino),
            "visitados" : len(visitados),
            "promedio_tiempo" : sum(suma_tiempo)/len(suma_tiempo),
            "numero_intentos" : len(suma_tiempo)
        }
        
        generar_imagen_con_solucion(laberinto_simple,camino,escala=12, output= "img_soluciones/BFS_SOLUCION.png")  
        imprimirSolucion(laberinto_simple,camino)
        # print(camino)
    
    # =========================================
    # UCS - Costo uniforme
    # =========================================
    elif opcion == "3":
        t_inicio = time.time()
        path, cost , visitados = ucs_camino(graph=grafo_ucs , start=inicio , goal=objetivo)
        f_inicio = time.time()

        tiempo["3"].append( f_inicio - t_inicio)
        suma_tiempo = tiempo['3']
        
        resumen["3"] = {
            "algoritmo" : "UCS COSTO UNIFORME",
            "tiempo" : f_inicio - t_inicio,
            "n_nodos_solucion" :  len(path),
            "costo_solucion" : cost,
            "visitados" : len(visitados),
            "promedio_tiempo" : sum(suma_tiempo)/len(suma_tiempo),
            "numero_intentos" : len(suma_tiempo)
        }
        
        imprimirSolucion(laberinto_costos,path)
        generar_imagen_con_solucion(laberinto_costos,path,escala=12, output="img_soluciones/UCS_SOLUCION.png")  

    # =========================================
    # A* - Búsqueda heurística
    # =========================================    
    elif opcion == "4":
        t_inicio = time.time()
        camino, costo_acumulado , visitados = a_estrella_camino( graph= grafo_estrella , heuristica = heuristica , start=inicio , goal=objetivo)
        f_inicio = time.time()

        tiempo["4"].append( f_inicio - t_inicio)
        suma_tiempo = tiempo['4']
        
        
        resumen["4"] = {
            "algoritmo" : "A* ESTRELLA HEURISTICA",
            "tiempo" : f_inicio - t_inicio,
            "n_nodos_solucion" :  len(camino),
            "costo_solucion" : costo_acumulado,
            "visitados" : len(visitados),
            "promedio_tiempo" : sum(suma_tiempo)/len(suma_tiempo),
            "numero_intentos" : len(suma_tiempo)
        }
        
        imprimirSolucion(laberinto_costos,camino)
        generar_imagen_con_solucion(laberinto_costos,camino,escala=12, output="img_soluciones/HEURISTICA_SOLUCION.png") 

        
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")


