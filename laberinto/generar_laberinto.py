import random

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

def generar(filas, columnas):
    matriz = construirLaberinto(filas, columnas)
    formatMatriz = parsearMatriz(matriz)
    return formatMatriz

# matriz = generar(29, 29)

# for i in range(len(matriz)):
#     print(matriz[i])