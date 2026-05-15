# IA-Proyecto

# Proyecto de Búsqueda en Laberintos

Este proyecto implementa diferentes algoritmos de búsqueda para resolver un laberinto representado como una matriz de `90x90`.

## Algoritmos implementados

- DFS (Búsqueda en profundidad)
- BFS (Búsqueda en amplitud)
- UCS (Costo uniforme)
- A* (Búsqueda heurística Manhattan)

El programa también genera imágenes `.png` con las soluciones encontradas.

---

# Requisitos

Tener instalado:

- Python 3

Verificar instalación:

```bash
python3 --version
```

---

# Ejecutar el proyecto

Desde la raíz del proyecto ejecutar:

```bash
python3 main.py
```

El programa se ejecutará en consola y mostrará un menú para seleccionar el algoritmo de búsqueda.

---

# Importante

El laberinto tiene un tamaño de `90x90`, por lo que se recomienda:

- Maximizar la ventana de la terminal
- Reducir el zoom de la consola si es necesario
- Utilizar la terminal en pantalla completa

Esto permitirá visualizar correctamente el laberinto y las soluciones en consola.

---

# Imágenes de soluciones

Cada vez que se ejecuta un algoritmo:

- Se genera una imagen `.png`
- La imagen muestra el camino encontrado sobre el laberinto

Las imágenes se guardan en la carpeta:

```bash
img_soluciones/
```

Ejemplos:

```bash
DFS_SOLUCION.png
BFS_SOLUCION.png
UCS_SOLUCION.png
HEURISTICA_SOLUCION.png
```

También se genera una imagen inicial del laberinto:

```bash
inicial.png
```

---

# Estructura general del proyecto

```bash
algoritmo/        -> Algoritmos de búsqueda
laberinto/        -> Matriz y acciones del laberinto
map/              -> Conversión de matriz a grafos
utils/            -> Generación y limpieza de imágenes
img_soluciones/   -> Imágenes generadas
main.py           -> Programa principal
menu.py           -> La estructura de los menus
```

---

# Funcionalidades

El programa permite:

- Resolver el laberinto con distintos algoritmos
- Comparar tiempos de ejecución
- Ver cantidad de nodos visitados
- Visualizar el camino encontrado
- Generar imágenes de las soluciones

---

# Nota

Las imágenes anteriores se eliminan automáticamente al iniciar el programa para evitar duplicados.