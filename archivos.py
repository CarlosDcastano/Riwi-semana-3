import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
    -----------
    inventario : list
        Lista de diccionarios donde cada diccionario representa un producto
        con claves 'nombre', 'precio' y 'cantidad'.
    ruta : str
        Ruta o nombre del archivo CSV donde se guardará el inventario.
    incluir_header : bool, opcional (por defecto True)
        Indica si se debe escribir la fila de encabezado al inicio del archivo.

    Retorno:
    --------
    None
        La función imprime mensajes de confirmación o error. No retorna valores.
    
    Notas:
    ------
    Maneja errores de permisos, ruta inexistente y errores genéricos durante la escritura.
    """
    # Validar inventario vacío
    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            # Escribir encabezado si así se pide
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            # Escribir cada producto
            for producto in inventario:
                escritor.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

    except PermissionError:
        print("Error: No tienes permisos para escribir en esa ubicación.")
    except FileNotFoundError:
        print("Error: La ruta especificada no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    else:
        print(f"Inventario guardado en: {ruta}")


def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV y valida su contenido.

    Parámetros:
    -----------
    ruta : str
        Ruta del archivo CSV a leer.

    Retorno:
    --------
    tuple:
        - List[dict]: Lista de productos válidos cargados desde el CSV, cada uno con
          claves 'nombre', 'precio' y 'cantidad'.
        - int: Número de filas inválidas que fueron omitidas.

    Notas:
    ------
    - Valida que el archivo tenga encabezado exacto: nombre, precio, cantidad.
    - Convierte 'precio' a float y 'cantidad' a int, y omite filas con valores negativos.
    - Maneja FileNotFoundError, UnicodeDecodeError, ValueError y otros errores genéricos.
    - Los nombres de los productos se almacenan en minúsculas y sin espacios al inicio/final.
    """
    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            
            # Leer encabezado
            encabezado = next(reader, None)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene un encabezado válido (nombre,precio,cantidad).")
                return [], 0

            # Procesar filas
            for fila in reader:
                # Validación 1: cantidad de columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    # Validación 2: valores no negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_cargados.append({
                        "nombre": nombre.lower().strip(),
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1
                    continue

        return productos_cargados, filas_invalidas

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except UnicodeDecodeError:
        print("Error: Problemas al leer el archivo (encoding inválido).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    return [], 0
