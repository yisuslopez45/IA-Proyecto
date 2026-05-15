"""
Funcion encargada de generar el grafo a partir de una matriz con costos, -
en donde la key es el nodo 'i,j' y el value en un arreglo de tuplas, en donde cada tupla 
representa el vecino junto con el costo que tomaria ir hasta el

Grafo de ejemplo
{
    '0.0': [('1.0', 3)],
    '1.0': [('1.1', 5), ('0.0', 3), ('2.0', 3)],
    ...
}
"""

def map_grafo(matriz):
    lenCol = len(matriz)
    grafo = {}
    for i in range(lenCol):
        lenRow = len(matriz[i])
        for j in range(lenRow):
            vecinos = []
            if matriz[i][j] != 0:
                if (j+1) <= (lenRow-1) and matriz[i][j+1] != 0:
                    index_vecino = f"{i}.{j+1}"
                    vecinos.append((index_vecino, matriz[i][j+1]))

                if (j-1) >= 0 and matriz[i][j-1] != 0:
                    index_vecino = f"{i}.{j-1}"
                    vecinos.append((index_vecino, matriz[i][j-1]))

                if(i+1) <= (lenCol-1) and matriz[i+1][j] != 0: 
                    index_vecino = f"{i+1}.{j}"
                    vecinos.append((index_vecino, matriz[i+1][j]))

                if(i-1) >= 0 and matriz[i-1][j] != 0: 
                    index_vecino = f"{i-1}.{j}"
                    vecinos.append((index_vecino, matriz[i-1][j])) 
                index = f"{i}.{j}"
                grafo[index] = vecinos
    return grafo