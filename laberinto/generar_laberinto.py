import random
import copy

"""
Funcion que se encarga de agregar costos de manera aleatoria al laberinto,
se agregan los costos a 1000 casillas del laberinto, los costos van de de 2 a 10.
"""
def addCostosLaberinto(laberinto):
    nCasillasConPeso = 1000
    laberintoPesos = copy.deepcopy(laberinto)
    while nCasillasConPeso > 0:
        costo =  random.randint(2,10)
        i = random.randint(1,90)
        j = random.randint(1,90)
        if laberintoPesos[i][j] == 1:
            laberintoPesos[i][j] = costo
            nCasillasConPeso -= 1
    
    return laberintoPesos

"""
Representacion de los costos del laberinto mediante iconos
0: muro
1: camino costo minimo
2 - 10: costos > 1
15: respresenta casilla que conforma la solucion
"""
iconsValsLaberinto = {
    0 : '🧱',
    1 : '⬛',
    2 : '🦔',
    3 : '🧨',
    4 : '🐊',
    5 : '🐌',
    6 : '🦧',
    7 : '🐛',
    8 : '🐧',
    9 : '🦥',
    10 : '🐢',
    15 : '🟩'
}

"""
Funcion encargada de imprimir salida inicial del laberinto
"""
def imprimirLaberinto(laberinto):
    for i in range(len(laberinto)):
        fila = []
        for j in range(len(laberinto[i])):
            if i == 90 and j == 90:
                fila.append('🏁')
            else:
                fila.append(iconsValsLaberinto[laberinto[i][j]])
        print(" ".join(fila))
    print("")

"""
Funcion encargada de pintar solucion en el laberinto, se pasa el laberinto generado
junto con la lista de nodos que conforman la solucion, se le asigna
"""
def imprimirSolucion(laberinto, camino):
    laberintoWithSolution = copy.deepcopy(laberinto)
    for i in range(len(camino)): 
        posicion = str(camino[i]).split(".")
        x = int(posicion[0])
        y = int(posicion[1])
        if laberintoWithSolution[x][y] == 1:
            laberintoWithSolution[x][y] = 15

    imprimirLaberinto(laberintoWithSolution)    
