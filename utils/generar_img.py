from PIL import Image
from laberinto.laberinto import laberinto as laberinto_simple
import copy


# Mapa de colores (RGB)
colores = {
    0: (50, 50, 50),     # pared 🧱
    1: (255, 255, 255), # camino ⬛
    2: (255, 200, 200),
    3: (255, 100, 100),
    4: (0, 200, 0),
    5: (200, 200, 0),
    6: (255, 150, 0),
    7: (150, 255, 150),
    8: (100, 100, 255),
    9: (150, 150, 150),
    10: (0, 150, 150),
    15: (255, 0, 255)
}

def generar_imagen_laberinto(laberinto, escala=8, output="laberinto.png"):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Crear imagen vacía
    img = Image.new("RGB", (columnas * escala, filas * escala))

    for i in range(filas):
        for j in range(columnas):
            valor = laberinto[i][j]

            # Meta
            if i == 90 and j == 90:
                color = (255, 0, 0)  # rojo 🏁
            else:
                color = colores.get(valor, (0, 0, 0))

            # Pintar bloque
            for x in range(escala):
                for y in range(escala):
                    img.putpixel((j * escala + x, i * escala + y), color)

    img.save(output)
    print(f"Imagen guardada como {output}")
    
    
    
def generar_imagen_con_solucion(laberinto, camino, escala=8, output="laberinto_sol.png"):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Copia para no dañar original
    lab = copy.deepcopy(laberinto)

    # 🔹 Pintar camino solución
    for nodo in camino:
        # soporta "x.y" o (x,y)
        if isinstance(nodo, str):
            x, y = map(int, nodo.split("."))
        else:
            x, y = nodo

        if lab[x][y] == 1:
            lab[x][y] = 15

    # Crear imagen
    img = Image.new("RGB", (columnas * escala, filas * escala))

    for i in range(filas):
        for j in range(columnas):
            if i == 90 and j == 90:
                color = (255, 0, 0)  # meta 🏁
            else:
                color = colores.get(lab[i][j], (0, 0, 0))

            # pintar bloque
            for dx in range(escala):
                for dy in range(escala):
                    img.putpixel((j * escala + dx, i * escala + dy), color)

    img.save(output)
    print(f"Imagen generada: {output}")  
    
    
    
# generar_imagen_laberinto(laberinto_simple)