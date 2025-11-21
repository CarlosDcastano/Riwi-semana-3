def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario si dicho producto no existe previamente.

    Parámetros:
    inventario (list): Lista de diccionarios que representan los productos existentes.
    nombre (str): Nombre del producto a agregar.
    precio (float): Precio del producto, debe ser positivo.
    cantidad (int): Cantidad del producto, debe ser positiva.

    Retorna:
    None
    """
    # Verifica si el producto ya existe en el inventario
    for pr in inventario:
        if pr["nombre"] == nombre:
            print("El producto ya existe, no es posible agregarlo, si desea actualizarlo, seleccione la opción de actualizar")
            return  

    # Crea un diccionario con los datos del nuevo producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agrega el producto al inventario
    inventario.append(producto)
    print("Producto agregado correctamente.")

        
def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en pantalla.

    Parámetros:
    inventario (list): Lista de diccionarios con los productos.

    Retorna:
    None
    """
    if not inventario:
        print("No hay productos por actualizar, inventario vacío")
    else:
        # Imprime cada producto con su nombre, precio y cantidad
        for producto in inventario:
            print(f"Nombre :{producto['nombre']} | Precio:{producto['precio']} | Cantidad:{producto['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario.

    Parámetros:
    inventario (list): Lista de diccionarios con los productos.
    nombre (str): Nombre del producto a buscar.

    Retorna:
    dict o None: Devuelve el producto encontrado o None si no existe.
    """
    if not inventario:
        return None
    else:
        # Recorre el inventario buscando coincidencia por nombre
        for producto in inventario:
            if nombre == producto["nombre"]:
                return producto


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.

    Parámetros:
    inventario (list): Lista de diccionarios con los productos.
    nombre (str): Nombre del producto a actualizar.
    nuevo_precio (float, opcional): Nuevo precio del producto.
    nueva_cantidad (int, opcional): Nueva cantidad del producto.

    Retorna:
    None
    """
    encontrado = False

    for producto in inventario:
        if producto["nombre"] == nombre:
            # Actualiza los valores del producto encontrado
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{nombre}' no existe en el inventario")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por su nombre.

    Parámetros:
    inventario (list): Lista de diccionarios con los productos.
    nombre (str): Nombre del producto a eliminar.

    Retorna:
    None
    """
    if not inventario:
        print("No hay productos por actualizar, inventario vacío")
        return

    encontrado = False

    for producto in inventario:
        if producto["nombre"] == nombre:
            # Elimina el producto encontrado
            inventario.remove(producto)
            print(f"Producto {producto['nombre']} eliminado")
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{nombre}' no existe en el inventario")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas básicas del inventario.

    Parámetros:
    inventario (list): Lista de diccionarios con los productos.

    Retorna:
    dict: Diccionario con las métricas:
        - unidades_totales (int)
        - valor_total (float)
        - producto_mas_caro (dict: nombre -> precio)
        - producto_mayor_stock (dict: nombre -> cantidad)
    """
    unidades_totales = 0
    precios = 0
    producto_mas_caro = 0
    mas_caro_nombre = ""
    producto_mayor_stock = 0
    mas_stock_nombre = ""
    total = 1

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        precios += producto["precio"]
        total += (unidades_totales * precios)

        # Determina el producto más caro
        if producto["precio"] >= producto_mas_caro:
            producto_mas_caro = producto["precio"]
            mas_caro_nombre = producto["nombre"]

        # Determina el producto con mayor stock
        if producto["cantidad"] >= producto_mayor_stock:
            producto_mayor_stock = producto["cantidad"]
            mas_stock_nombre = producto["nombre"]

    est = {
        "unidades_totales": unidades_totales,
        "valor_total": total,
        "producto_mas_caro": {mas_caro_nombre: producto_mas_caro},
        "producto_mayor_stock": {mas_stock_nombre: producto_mayor_stock}
          }


    




