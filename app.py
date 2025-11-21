from servicios import *
from archivos import *

def menu():
    print(f"#" * 50)
    print("                MENÚ DE OPCIONES")
    print("                1. Agregar")
    print("                2. Mostrar")
    print("                3. Buscar")
    print("                4. Actualizar")
    print("                5. Eliminar")
    print("                6. Estadísticasr")
    print("                7. Guardar CSV")
    print("                8. Cargar CSV")
    print("                9. Salir")

def main():
    
    while True:
        menu()
        try:
            opcion = int(input("Por favor seleccione una de las opciones del menú a realizar: ")) 
        except ValueError:
            print("Debe ingresar un valor numérico dentro del menú")
        else:
            if opcion in range(1,10):
                if opcion == 1:
                    while True:
                        try:
                            nombre = input("Ingrese el nombre del producto: ").lower()
                            precio = float(input("Ingrese el precio del producto: "))
                            cantidad = int(input("Ingrese la cantidad de productos: "))

                            if precio <= 0 or cantidad <= 0:
                                print("Precio y cantidad deben ser valores positivos.")
                                continue
                        except ValueError:
                            print("Valide que precio sea un valor entero o decimal y cantidad solo puede ser un valor entero")
                        else:

                            agregar_producto(inventario, nombre, precio, cantidad)
                            break


                elif opcion == 2:
                        mostrar_inventario(inventario)
                    
                elif opcion == 3:         
                    nombre = input("Ingrese el nombre del producto a buscar: ").lower()
                    print(buscar_producto(inventario, nombre))

                elif opcion == 4:
                    if not inventario:
                        print("No hay productos por actualizar, inventario vacío")
                    else:
                        while True:
                            try:
                                nombre = input("Ingrese el nombre del producto a actualizar: ").lower()
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                nueva_cantidad = int(input("Ingrese la nueva cantidad de productos: "))

                                if precio <= 0 or cantidad <= 0:
                                    print("Precio y cantidad deben ser valores positivos.")
                                    continue
                            except ValueError:
                                print("Valide que precio sea un valor entero o decimal y cantidad solo puede ser un valor entero")
                            else:
                                actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                                break
                    
                elif opcion == 5:
                    nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
                    eliminar_producto(inventario, nombre)

                elif opcion == 6:
                    est = (calcular_estadisticas(inventario))
                    for clave, valor in est.items():
                        print(clave, ":", valor)

                elif opcion == 7:
                    ruta = input("Ingrese el nombre o ruta del archivo CSV a guardar: ")
                    guardar_csv(inventario, ruta)

                elif opcion == 8:
                    ruta = input("Ruta del archivo CSV a cargar: ")

                    nuevos, errores = cargar_csv(ruta)

                    if not nuevos:
                        print("No se cargaron productos.")
                        continue
                    
                    print(f"Archivo cargado. {len(nuevos)} productos válidos, {errores} filas inválidas.")

                    # Pregunto al usuario si desea sobrescribir
                    decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

                    if decision == "S":
                        inventario[:] = nuevos
                        print("Inventario reemplazado completamente.")

                    elif decision == "N":
                        print("Fusionando inventario...")

                        # Política de fusión: 
                        # - Si el nombre existe → suma cantidades, actualiza precio al nuevo.
                        # - Si no existe → agregarlo.
                        for nuevo in nuevos:
                            existe = False
                            for prod in inventario:
                                if prod["nombre"] == nuevo["nombre"]:
                                    prod["cantidad"] += nuevo["cantidad"]  # suma stock
                                    prod["precio"] = nuevo["precio"]       # actualiza precio
                                    existe = True
                                    break
                            if not existe:
                                inventario.append(nuevo)

                        print("Inventario fusionado correctamente.")

                    else:
                        print("Opción no válida. No se hicieron cambios.")

                    print(f"Resumen:")
                    print(f"  Productos cargados: {len(nuevos)}")
                    print(f"  Filas inválidas: {errores}")
                    print(f"  Acción: {'Reemplazo' if decision=='S' else 'Fusión' if decision=='N' else 'Ninguna'}")

                else:
                    print("Adios")
                    break
            else:
                print("Opción no válida, ingrese un número dentro del menú")
        
inventario = []
main()
                