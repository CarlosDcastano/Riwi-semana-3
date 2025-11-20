def agregar_producto(inventario, nombre, precio, cantidad):
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("El producto ya existe, no es posible agregarlo, si desea actualizarlo, seleccione la opción de actualizar")
    
        else:
            producto = {
                "nombre" : nombre,
                "precio" : precio,
                "cantidad": cantidad
                }

    inventario.append(producto)
        
def mostrar_inventario(inventario):
    if not inventario:
        print(inventario, "vacío")
    else:
        for producto in inventario:
            print(f"Nombre :{producto['nombre']} | Precio:{producto['precio']} | Cantidad:{producto['cantidad']}")

def buscar_producto(inventario, nombre):
    if not inventario:
        return None
    else:
        for producto in inventario:
            if nombre == producto["nombre"]:
                return producto
            
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    if not inventario:
        print(inventario, "vacío")
    else:
        for producto in inventario:
            if producto["nombre"] == nombre:
                producto #VOY AQUI

    
