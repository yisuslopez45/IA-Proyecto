laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
]

def map_grafo(matriz):
    lenCol = len(matriz)
    grafo = {}
    for i in range(lenCol):
        lenRow = len(matriz[i])
        for j in range(lenRow):
            vecinos = []
            if matriz[i][j] != 0:
                if (j+1) <= (lenRow-1) and matriz[i][j+1] != 0:
                    index_vecino = float(f"{i}.{j+1}")
                    vecinos.append((index_vecino, matriz[i][j+1]))

                if (j-1) >= 0 and matriz[i][j-1] != 0:
                    index_vecino = float(f"{i}.{j-1}")
                    vecinos.append((index_vecino, matriz[i][j-1]))
                
                if(i+1) <= (lenCol-1) and matriz[i+1][j] != 0: 
                    index_vecino = float(f"{i+1}.{j}")
                    vecinos.append((index_vecino, matriz[i+1][j]))

                if(i-1) >= 0 and matriz[i-1][j] != 0: 
                    index_vecino = float(f"{i-1}.{j}")
                    vecinos.append((index_vecino, matriz[i-1][j]))
                index = float(f"{i}.{j}")
                grafo[index] = vecinos
    return grafo

print(map_grafo(laberinto))