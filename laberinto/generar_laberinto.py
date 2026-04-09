import random
import copy
#########################################################
# CREDITOS ALGORITMO PARA GENERAR LABERINTO
# REPOSITORIO: https://github.com/gittoni09/laberinto
# Create, print and resolve a console based laberinth
# python3 laberinto.py 
# 2020 - Antonio Royo Moraga
#########################################################

def parsearMatriz(matriz):
    MATRIZ = []
    for i  in range(len(matriz)):
        clearList = [item for item in list(matriz[i]) if item != " "]
        if(len(clearList) > 0):
            MATRIZ.append([int(item) for item in clearList])
    return MATRIZ

def numCaminos(fila, col, MATRIZ, nCols, nFilas, WALL_DELIMITER):
    caminos = 0
    if (fila+2) < nFilas :
        if MATRIZ[fila+2][col] == WALL_DELIMITER: caminos += 1
    if (fila-2) >= 0:
        if MATRIZ[fila-2][col] == WALL_DELIMITER: caminos += 1
    if (col+2) < (nCols -2):
        if MATRIZ[fila][col+2] == WALL_DELIMITER: caminos += 1
    if (col-2) >= 0:
        if MATRIZ[fila][col-2] == WALL_DELIMITER: caminos += 1

    return caminos

def guardaPosic(fila, col):
    return [fila, col]

def construirLaberinto(filas, columnas):
    WALL_DELIMITER = "0"
    LABERINTH_PATH = "1"

    nColumnas = filas 
    nFilas = columnas

    MATRIZ = []
    MATRIZ.append(" "*nColumnas)
    for i in range (1,nColumnas-1,1):
        MATRIZ.append(" " + WALL_DELIMITER*(nColumnas - 2 ) +" ")
    MATRIZ.append(" "*nColumnas)
    
    #CONTADOR DE DIRECCIONES
    C = []
    C.append([0,0])
    finalizado = False

    #POSICION INICIAL DE DONDE SE EMPIEZA A CONSTRUIR LA MATRIZ 
    inicioFila = 15
    inicioCol = 15
    MATRIZ[inicioFila] = MATRIZ[inicioFila-1][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila-1][inicioCol+1:]

    while not(finalizado):
        LI = numCaminos(inicioFila, inicioCol, MATRIZ, nColumnas, nFilas, WALL_DELIMITER)
        if LI == 0: 
            temp = C.pop()
            inicioFila = temp[0]
            inicioCol = temp[1]
            if inicioCol == 0 and inicioFila == 0:
                finalizado = True
        elif LI > 1:
            avanzado = False
            while not (avanzado):
                if (random.random() > 0.6 and inicioFila-2 > 0):
                    if (MATRIZ[inicioFila-2][inicioCol] == WALL_DELIMITER):
                        MATRIZ[inicioFila-1] = MATRIZ[inicioFila-1][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila-1][inicioCol+1:]
                        MATRIZ[inicioFila-2] = MATRIZ[inicioFila-2][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila-2][inicioCol+1:]
                        inicioFila -= 2
                        C.append(guardaPosic(inicioFila,inicioCol))
                        avanzado = True
                elif (random.random() > 0.5 and inicioCol+2 < nColumnas):
                    if (MATRIZ[inicioFila][inicioCol+2] == WALL_DELIMITER):
                        MATRIZ[inicioFila] = MATRIZ[inicioFila][:inicioCol] + "11" + MATRIZ[inicioFila][inicioCol+2:]
                        inicioCol += 2
                        C.append(guardaPosic(inicioFila,inicioCol))
                        avanzado = True
                elif (random.random() > 0.4 and inicioFila+2 < nFilas):
                    if (MATRIZ[inicioFila+2][inicioCol] == WALL_DELIMITER):
                        MATRIZ[inicioFila+1] = MATRIZ[inicioFila+1][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila+1][inicioCol+1:]
                        MATRIZ[inicioFila+2] = MATRIZ[inicioFila+2][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila+2][inicioCol+1:]
                        inicioFila += 2
                        C.append(guardaPosic(inicioFila,inicioCol))
                        avanzado = True
                elif (random.random() > 0.3 and inicioCol-2 > 0):
                    if (MATRIZ[inicioFila][inicioCol-2] == WALL_DELIMITER):
                        MATRIZ[inicioFila] = MATRIZ[inicioFila][:inicioCol-2] + "11" + MATRIZ[inicioFila][inicioCol:]
                        inicioCol -= 2
                        C.append(guardaPosic(inicioFila,inicioCol))
                        avanzado = True
        elif LI == 1:
            if (random.random() > 0.6 and inicioFila-2 > 0):
                if (MATRIZ[inicioFila-2][inicioCol] == WALL_DELIMITER):
                    MATRIZ[inicioFila-1] = MATRIZ[inicioFila-1][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila-1][inicioCol+1:]
                    MATRIZ[inicioFila-2] = MATRIZ[inicioFila-2][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila-2][inicioCol+1:]
                    inicioFila -= 2
                    C.append(guardaPosic(inicioFila,inicioCol))
                    avanzado = True
            elif (random.random() > 0.5 and inicioCol+2 < nColumnas):
                if (MATRIZ[inicioFila][inicioCol+2] == WALL_DELIMITER):
                    MATRIZ[inicioFila] = MATRIZ[inicioFila][:inicioCol] + "11" + MATRIZ[inicioFila][inicioCol+2:]
                    inicioCol += 2
                    C.append(guardaPosic(inicioFila,inicioCol))
                    avanzado = True
            elif (random.random() > 0.4 and inicioFila+2 < nFilas):
                if (MATRIZ[inicioFila+2][inicioCol] == WALL_DELIMITER):
                    MATRIZ[inicioFila+1] = MATRIZ[inicioFila+1][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila+1][inicioCol+1:]
                    MATRIZ[inicioFila+2] = MATRIZ[inicioFila+2][:inicioCol] + LABERINTH_PATH + MATRIZ[inicioFila+2][inicioCol+1:]
                    inicioFila += 2
                    C.append(guardaPosic(inicioFila,inicioCol))
                    avanzado = True
            elif (random.random() > 0.3 and inicioCol-2 > 0):
                if (MATRIZ[inicioFila][inicioCol-2] == WALL_DELIMITER):
                    MATRIZ[inicioFila] = MATRIZ[inicioFila][:inicioCol-2] + "11" + MATRIZ[inicioFila][inicioCol:]
                    inicioCol -= 2
                    C.append(guardaPosic(inicioFila,inicioCol))
                    avanzado = True
    return MATRIZ

def randomLaberinto():
    matriz = construirLaberinto(29, 29)
    formatMatriz = parsearMatriz(matriz)
    if(formatMatriz[0][0] == 0 or formatMatriz[26][26] == 0):
        return randomLaberinto()
    return formatMatriz


def addCostosLaberinto(laberinto):
    nCasillasConPeso = 30
    laberintoPesos = copy.deepcopy(laberinto)
    while nCasillasConPeso > 0:
        costo = random.randint(2,10)
        i = random.randint(1,25)
        j = random.randint(1,25)
        if laberintoPesos[i][j] == 1:
            laberintoPesos[i][j] = costo
            nCasillasConPeso -= 1
    
    return laberintoPesos

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

def imprimirLaberinto(laberinto):
    for i in range(len(laberinto)):
        fila = []
        for j in range(len(laberinto[i])):
            if i == 26 and j == 26:
                fila.append('🏁')
            else:
                fila.append(iconsValsLaberinto[laberinto[i][j]])
        print(" ".join(fila))
    print("")

def imprimirSolucion(laberinto, camino):
    laberintoWithSolution = copy.deepcopy(laberinto)
    for i in range(len(camino)): 
        posicion = str(camino[i]).split(".")
        x = int(posicion[0])
        y = int(posicion[1])
        if laberintoWithSolution[x][y] == 1:
            laberintoWithSolution[x][y] = 15

    imprimirLaberinto(laberintoWithSolution)    





# maze = addCostosLaberinto(randomLaberinto())
# imprimirLaberinto(maze)