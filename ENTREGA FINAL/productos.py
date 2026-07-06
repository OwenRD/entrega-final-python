from database import cursor, conexion
from utils import validar_producto, validar_num, encontrar_producto

def agregar_producto():
    print("\n")
    print("| Agregar Producto |")
    print("\n")

    producto = ["", "", "", "", ""]

    producto[0] = input("Nombre: ").strip()
    producto[1] = input("Categoria: ").strip()
    producto[2] = input("Precio: ").strip()
    producto[3] = input("Descripcion (Opcional): ").strip()
    producto[4] = input("Cantidad: ").strip()

    try:
        flag = validar_producto(producto)

        if flag:
            producto = flag
        else:
            return

        cursor.execute(
            """
                INSERT INTO productos(nombre, categoria, precio, descripcion, cantidad)
                VALUES(?,?,?,?,?)
            """,
            (producto[0], producto[1], producto[2], producto[3], producto[4])
        )

        conexion.commit()
        
        print("\n")
        print("Se agrego el producto con exito :)")
        print("\n")
    
    except ValueError as err:
        print(err)

    


def ver_productos():
    print("\n")
    print("| Ver Productos |")
    print("\n")

    try:

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    except ValueError as err:
        print(err)

    if len(productos) > 0:
        for i, producto in enumerate(productos, start=1):
            print(f"|| ID: {producto[0]} | NOM: {producto[1]} | CAT: {producto[2]} | PRE: {producto[4]} $ | DES: {producto[3]} | CAN: {producto[5]} ||")
    else:
        print("No hay productos :(")


        


def editar_producto():
    print("\n")
    print("| Editar Producto |")
    print("\n")

    try:

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    except ValueError as err:
        print(err)

    if len(productos) == 0:
        print("No hay productos :(")
        return
    else:
        print("Productos disponibles: \n")
        for i, producto in enumerate(productos, start=1):
            print(f"|| ID: {producto[0]} | NOM: {producto[1]} | CAT: {producto[2]} | PRE: {producto[4]} $ | DES: {producto[3]} | CAN: {producto[5]} ||")
        
        print("Ingrese el ID del producto que desea Editar")
        id = input("> ")

        id = validar_num(id)
        
        if id:
            
            if encontrar_producto(productos, id):

                print("Ingrese los nuevos datos del producto:")

                producto = ["", "", "", "", ""]

                producto[0] = input("Nombre: ").strip()
                producto[1] = input("Categoria: ").strip()
                producto[2] = input("Precio: ").strip()
                producto[3] = input("Descripcion (Opcional): ").strip()
                producto[4] = input("Cantidad: ").strip()

                if validar_producto(producto):

                    try:
                        cursor.execute(
                        """
                            UPDATE productos
                            SET nombre = ?, categoria = ?, precio = ?, descripcion = ?, cantidad = ?
                            WHERE id = ?
                        """,
                        (producto[0], producto[1], producto[2], producto[3], producto[4], id)
                        )

                        conexion.commit()

                        print("\n")
                        print("Ya se establecio los nuevos datos")
                        print("\n")
                    except ValueError as err:
                        print(err)
                        return



def eliminar_producto():
    print("\n")
    print("| Eliminar Producto |")
    print("\n")

    try:

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    except ValueError as err:
        print(err)

    if len(productos) == 0:
        print("No hay productos :(")
        return
    else:
        print("Productos disponibles: \n")
        for i, producto in enumerate(productos, start=1):
            print(f"|| ID: {producto[0]} | NOM: {producto[1]} | CAT: {producto[2]} | PRE: {producto[4]} $ | DES: {producto[3]} | CAN: {producto[5]} ||")

        print("Ingrese el ID del producto que desea Eliminar")
        id = input("> ")

        id = validar_num(id)

        if id:

            if encontrar_producto(productos, id):

                try:

                    cursor.execute(
                        """
                            DELETE FROM productos
                            WHERE id = ?
                        """,
                        (id,)
                    )

                    conexion.commit()

                    print("\n")
                    print("Se elimino el producto con exito ;)")
                    print("\n")

                except ValueError as err:
                    print(err)

            

def buscar_producto():
    print("\n")
    print("| Buscar Producto |")
    print("\n")

    try:

        print("Ingrese el ID del producto que desea encontrar")
        id = input("> ")

        if validar_num(id):

            cursor.execute(
                """
                    SELECT *
                    FROM productos
                    WHERE id = ?
                """,
                (id,)
            )
            producto = cursor.fetchall()

            if len(producto) > 0:
                print(f"|| ID: {producto[0][0]} | NOM: {producto[0][1]} | CAT: {producto[0][2]} | PRE: {producto[0][4]} $ | DES: {producto[0][3]} | CAN: {producto[0][5]} ||")
            else:
                print("No se encontro el producto :(")

    except ValueError as err:
        print(err)

def reporte_de_productos():
    print("\n")
    print("| Reporte de Productos |")
    print("\n")

    print("\nBuscar productos por cantidad")
    print("Ingrese el dato")
    cant = input("> ")

    cant = validar_num(cant)

    if cant or cant == 0:
        try:

            cursor.execute(
                """
                    SELECT *
                    FROM productos
                    WHERE cantidad <= ?
                """,
                (cant,)
            )

            productos = cursor.fetchall()

            if len(productos) > 0:
                for i, producto in enumerate(productos, start=1):
                    print(f"|| ID: {producto[0]} | NOM: {producto[1]} | CAT: {producto[2]} | PRE: {producto[4]} $ | DES: {producto[3]} | CAN: {producto[5]} ||")
            else:
                print("No se encontro productos")

        except ValueError as err:
            print(err)