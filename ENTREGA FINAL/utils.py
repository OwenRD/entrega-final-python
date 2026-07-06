def validar_precio(txt):

    try:

        precio = float(txt)
    
    except ValueError:

        print("El precio debe contener solo numeros")
        return False
    
    if precio < 0:
        print("El presio no debe contener numeros negativos")
        return False

    return precio 


def validar_num(txt):
    
    try:

        num = int(txt)

    except ValueError:

        print("El contenido debe ser numerico")
        return False
    
    if num < 0:
        print("El contenido no debe contener numeros negativos")
        return False
    
    return num

def validar_producto(producto):

    if producto[0] == "":
        print("NO debe haber campos vacios")
        return False
    
    if producto[1] == "":
        print("NO debe haber campos vacios")
        return False
    
    if producto[2] == "":
        print("NO debe haber campos vacios")
        return False
    
    flag1 = validar_precio(producto[2])

    if not flag1:
        print("Error en validar_producto()")
        return False
    else:
        producto[2] = flag1 
    
    if producto[4] == "":
        print("NO debe haber campos vacios")
        return False
    
    flag2 = validar_num(producto[4])

    if not flag2:
        print("Error en validar_producto()")
        return False
    else:
        producto[4] = flag2

    return producto

def encontrar_producto(productos, id):

    for producto in productos:
        if id == producto[0]:
            return True
        
    print("\nEse producto NO se encunetra")
    return False