import random

WALL_DELIMITER = "0"
LABERINTH_PATH = "1"

maxH = 29 
maxV = 29
A = []
A.append(" "*maxH)
for i in range (1,maxV-1,1):
    A.append(" " + WALL_DELIMITER*(maxH - 2 ) +" ")
A.append(" "*maxH)

C = []
C.append([0,0])
finalizado = False

#POSICION INICIAL DE DONDE SE EMPIEZA A CONSTRUIR LA MATRIZ 
V = 13
H = 3

A[V] = A [V-1][:H] + LABERINTH_PATH + A [V-1][H+1:]

def numCaminos(V, H, A, maxH, maxV):
    caminos = 0
    if (V+2) < maxV :
        if A[V+2][H] == WALL_DELIMITER: caminos += 1
    if (V-2) >= 0:
        if A[V-2][H] == WALL_DELIMITER: caminos += 1
    if (H+2) < (maxH -2):
        if A[V][H+2] == WALL_DELIMITER: caminos += 1
    if (H-2) >= 0:
        if A[V][H-2] == WALL_DELIMITER: caminos += 1

    return caminos

def guardaPosic(V, H):
    return [V, H]

while not(finalizado):
    LI = numCaminos(V, H, A, maxH, maxV)
    if LI == 0: 
        temp = C.pop()
        V = temp[0]
        H = temp[1]
        if H == 0 and V == 0:
            finalizado = True
    elif LI > 1:
        avanzando = False
        while not (avanzando):
            if (random.random() > 0.6 and V-2 > 0):
                if (A[V-2][H] == WALL_DELIMITER):
                    A[V-1] = A [V-1][:H] + LABERINTH_PATH + A [V-1][H+1:]
                    A[V-2] = A [V-2][:H] + LABERINTH_PATH + A [V-2][H+1:]
                    V -= 2
                    C.append(guardaPosic(V,H))
                    avanzando = True
            elif (random.random() > 0.5 and H+2 < maxH):
                if (A[V][H+2] == WALL_DELIMITER):
                    A[V] = A [V][:H] + "11" + A [V][H+2:]
                    H += 2
                    C.append(guardaPosic(V,H))
                    avanzando = True
            elif (random.random() > 0.4 and V+2 < maxV):
                if (A[V+2][H] == WALL_DELIMITER):
                    A[V+1] = A [V+1][:H] + LABERINTH_PATH + A [V+1][H+1:]
                    A[V+2] = A [V+2][:H] + LABERINTH_PATH + A [V+2][H+1:]
                    V += 2
                    C.append(guardaPosic(V,H))
                    avanzando = True
            elif (random.random() > 0.3 and H-2 > 0):
                if (A[V][H-2] == WALL_DELIMITER):
                    A[V] = A [V][:H-2] + "11" + A [V][H:]
                    H -= 2
                    C.append(guardaPosic(V,H))
                    avanzando = True
    elif LI == 1: #What happens if there are more than one open path
        if (random.random() > 0.6 and V-2 > 0):
            if (A[V-2][H] == WALL_DELIMITER):
                A[V-1] = A [V-1][:H] + LABERINTH_PATH + A [V-1][H+1:]
                A[V-2] = A [V-2][:H] + LABERINTH_PATH + A [V-2][H+1:]
                V -= 2
                C.append(guardaPosic(V,H))
                avanzando = True
        elif (random.random() > 0.5 and H+2 < maxH):
            if (A[V][H+2] == WALL_DELIMITER):
                A[V] = A [V][:H] + "11" + A [V][H+2:]
                H += 2
                C.append(guardaPosic(V,H))
                avanzando = True
        elif (random.random() > 0.4 and V+2 < maxV):
            if (A[V+2][H] == WALL_DELIMITER):
                A[V+1] = A [V+1][:H] + LABERINTH_PATH + A [V+1][H+1:]
                A[V+2] = A [V+2][:H] + LABERINTH_PATH + A [V+2][H+1:]
                V += 2
                C.append(guardaPosic(V,H))
                avanzando = True
        elif (random.random() > 0.3 and H-2 > 0):
            if (A[V][H-2] == WALL_DELIMITER):
                A[V] = A [V][:H-2] + "11" + A [V][H:]
                H -= 2
                C.append(guardaPosic(V,H))
                avanzando = True

MATRIZ = []

for i  in range(len(A)):
    clearList = [item for item in list(A[i]) if item != " "]
    if(len(clearList) > 0):
        MATRIZ.append([int(item) for item in clearList])
        print([int(item) for item in clearList])


