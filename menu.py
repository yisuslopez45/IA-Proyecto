def mostrar_menu(RESUMEN):
    
    if not RESUMEN:
        print("NO SE ENCONTRARON SOLUCIONES..!!")
    else:
        imprimir_tabla(RESUMEN)
    
    print("\n------ MENÚ PRINCIPAL --------")
    print("1. Busqueda por profundidad")
    print("2. Busqueda por amplitud")
    print("3. Busqueda por costo uniforme")
    print("4. Busqueda por a* Estrella")
    print("5. Salir")












def imprimir_tabla(resumen):
    # Encabezados
    headers = ["ID", "Algoritmo", "Tiempo (s)", "Nodos Solución", "Costo Solución"]

    # Preparar filas
    filas = []
    for k, v in resumen.items():
        filas.append([
            k,
            v.get("algoritmo", "-"),
            f"{v.get('tiempo', 0):.6f}",
            v.get("n_nodos_solucion", "-"),
            v.get("costo_solucion", "-")
        ])

    # Calcular ancho de columnas
    col_widths = [len(h) for h in headers]
    for fila in filas:
        for i, val in enumerate(fila):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Función para imprimir línea
    def print_line():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    # Función para imprimir fila
    def print_row(row):
        print("| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |")

    # Imprimir tabla
    print_line()
    print_row(headers)
    print_line()
    for fila in filas:
        print_row(fila)
    print_line()