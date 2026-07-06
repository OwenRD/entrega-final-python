from database import crear_tabla, cerrar_conexion

from productos import agregar_producto
from productos import ver_productos
from productos import editar_producto
from productos import eliminar_producto
from productos import buscar_producto
from productos import reporte_de_productos

crear_tabla()
productos = [1]
while True:
    print("\n=== MENU ===")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Editar producto")
    print("4. Eliminar productos")
    print("5. Buscar en base a ID")
    print("6. Reporte por cantidad")
    print("7. Salir")
    print("============\n")

    entrada = input("Seleccione opcion\n > ")

    if not entrada.isdigit():
        print("Debe ingresar un numero\n")
        continue
    else : 
        op = int(entrada)

    if op < 1 or op > 7 :
        print("Opcion invalida\n")
        continue

    match op:
        case 1:
            agregar_producto()
        case 2:
            ver_productos()
        case 3:
            editar_producto()
        case 4:
            eliminar_producto()
        case 5:
            buscar_producto()
        case 6:
            reporte_de_productos()
        case 7:
            break

cerrar_conexion()
        