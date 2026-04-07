import time
import curses
from curses import wrapper
import random

#Constants
WALL_DELIMITER = "#"
LABERINTH_PATH = "O"
SOLUTION_PATH = "*"

maxH = 35 
maxV = 23

A = []
A.append("                                   ")
for i in range (1,maxV-1,1):
    A.append(" ################################# ")
A.append("                                   ")

C = []
C.append([0,0])
#Flag to end the main loop
finalizado = False
#Start position is initially assigned
V = 13
H = 3
A [V] = A [V-1][:H] + LABERINTH_PATH + A [V-1][H+1:]

print(A)
print(C)

def numCaminos():
    # nonlocal V
    # nonlocal H
    # nonlocal A
    # nonlocal maxH
    # nonlocal maxV
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