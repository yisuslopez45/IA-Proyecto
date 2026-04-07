import random

# Constantes
WALL = "#"
PATH = "O"

maxH = 35
maxV = 23

# Crear matriz (lista de strings)
A = []

for _ in range(1, maxV - 1):
    A.append(" " + WALL * (maxH - 2) + " ")


# Posición inicial
V, H = 13, 3

# Convertir string a lista para poder modificar fácilmente
A = [list(row) for row in A]

# Marcar inicio
A[V][H] = PATH

# Pila para backtracking
stack = [(V, H)]

def vecinos_validos(V, H):
    dirs = []

    if V - 2 > 0 and A[V - 2][H] == WALL:
        dirs.append(("up", V - 2, H))
    if H + 2 < maxH - 1 and A[V][H + 2] == WALL:
        dirs.append(("right", V, H + 2))
    if V + 2 < maxV - 1 and A[V + 2][H] == WALL:
        dirs.append(("down", V + 2, H))
    if H - 2 > 0 and A[V][H - 2] == WALL:
        dirs.append(("left", V, H - 2))

    return dirs

while stack:
    V, H = stack[-1]

    vecinos = vecinos_validos(V, H)

    if not vecinos:
        # Backtracking
        stack.pop()
        continue

    # Elegir dirección aleatoria válida
    dir, newV, newH = random.choice(vecinos)

    # Romper pared intermedia
    midV = (V + newV) // 2
    midH = (H + newH) // 2

    A[midV][midH] = PATH
    A[newV][newH] = PATH

    stack.append((newV, newH))

print(A)
# Convertir de nuevo a string para imprimir
A = ["".join(row) for row in A]

# Mostrar laberinto
for row in A:
    print(row)