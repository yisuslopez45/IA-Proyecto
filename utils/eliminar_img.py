from pathlib import Path

def limpiar_imagenes_soluciones():
    carpeta = Path("img_soluciones")

    if not carpeta.exists():
        print("La carpeta no existe:", carpeta)
        return

    if not carpeta.is_dir():
        print("La ruta no es una carpeta:", carpeta)
        return

    eliminados = 0

    for archivo in carpeta.glob("*.png"):
        try:
            archivo.unlink()
            eliminados += 1
        except Exception as e:
            print(f"Error eliminando {archivo.name}: {e}")

    print(f"Se eliminaron {eliminados} archivos .png")