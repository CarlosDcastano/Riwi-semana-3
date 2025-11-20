from servicios import *

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
            if opcion in range(1,10):
                if opcion == 1:
                    while True:
                        try:
                            nombre = input("Ingrese el nombre del producto: ").lower()
                            precio = float(input("Ingrese el precio del producto: "))
                            cantidad = int(input("Ingrese la cantidad de productos: "))
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
                            except ValueError:
                                print("Valide que precio sea un valor entero o decimal y cantidad solo puede ser un valor entero")
                            else:
                                actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                                break
                    
                elif opcion == 5:
                    pass
                elif opcion == 6:
                    pass
                elif opcion == 7:
                    pass
                elif opcion == 8:
                    pass
                else:
                    print("Adios")
                    break
            else:
                print("Opción no válida, ingrese un número dentro del menú")
        except ValueError:
            print("Debe ingresar un valor numérico dentro del menú")
            print("")
inventario = []
main()
                