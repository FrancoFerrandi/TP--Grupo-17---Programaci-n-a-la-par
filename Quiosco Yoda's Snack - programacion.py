MENU = """
Seleccione el numero de alguna de las siguientes opciones:
1) Agregar producto al inventario.
2) Realizar una venta.
3) Mostrar productos disponibles.
4) Salir del sistema.
"""


inventario = [["agua", 100, 1000],["coca", 1000, 150],["chupetines", 15, 100]]

def llamar_menu(menu:str) -> str:
    """
    Recibe parametro menu e imprime el string de menu.
    Parametros: menu (str)
    Salida: menu (str)
    """
    print(menu)

def agregar_producto(inventario:list) -> list:
    """
    Recibe parametro una lista("inventario"), genera una lista nueva con nombre de producto, cantidad y precio y luego anida lista nueva en la lista recibida como parametro.
    Parametros: inventario (list)
    Salida: inventario (list)
    """

    lista_producto_nuevo = []
    producto_nombre = (input("Ingrese el nombre del producto: ")).lower()
    while producto_nombre == "" and producto_nombre != str:
        producto_nombre = str(input("Nombre no valido. Ingrese el nombre del producto: ")).lower()

    producto_cantidad = int(input("Ingrese la cantidad de producto que desea agregar al inventario: "))
    while producto_cantidad <= 0:
        producto_cantidad = int(input("Cantidad no valida. Reingrese la cantidad de producto que desea agregar al inventario: "))
    
    producto_precio = float(input("Ingrese el precio del producto que desea agregar al inventario: "))
    while producto_precio <= 0:
        producto_precio = float(input("Precio invalido. Reingrese el precio de producto que desea agregar al inventario: "))

    lista_producto_nuevo = [producto_nombre, producto_precio, producto_cantidad]
    inventario.append(lista_producto_nuevo)
    
    return inventario

def mostrar_productos_disponibles(inventario:list) -> str:
    """
    Recibe parametro una lista("inventario") e imprime cada una de las listas anidadas dentro de esa lista.
    Parametros: inventario (list)
    Salida: producto (str)
    """
    for n in range(len(inventario)):
        producto = f"Producto: {inventario[n][0]}, precio unitario: {inventario[n][1]}, cantidad disponible: {inventario[n][2]}."
        print(producto)

def ejecutar_venta(inventario:list) -> str: 
    """
    Recibe parametro una lista("inventario"), verifica valores de la misma y devuelve mensaje si es posible o no la venta.
    Parametros: inventario (list)
    Salida: mensaje (str)
    """
    eleccion_producto = input("Que producto eliges? ")
    producto_encontrado = False

    for n in range(len(inventario)):
        if eleccion_producto == inventario[n][0]:
            producto_encontrado = True
            cantidad_producto = int(input("Cuanto producto deseas llevar? "))
    
            if cantidad_producto <= inventario[n][2]:
                inventario[n][2] -= cantidad_producto
                total_a_pagar = cantidad_producto * inventario[n][1]
                mensaje = f"Producto comprado exitosamente. Queda {inventario[n][2]} unidades de {eleccion_producto}. Total a pagar por el cliente: ${total_a_pagar}."
                print(mensaje)
            else:
                mensaje = f"No hay suficiente stock. Solo hay {inventario[n][2]} unidades."
                print(mensaje)
            break
    if producto_encontrado == False:
        mensaje = "Producto no disponible en el inventario"
        print()

def ejecutar_opcion(seguir:bool) -> bool:
    """
    Recibe parametro "seguir" (bool), se le pregunta un numero de opcion y ejecuta esa opcion(funcion) o finaliza el programa.
    Parametros: seguir (bool)
    Salida: seguir (bool)
    """
    opcion = int(input("Elige una opcion: "))
    while opcion < 1 or opcion > 4: 
        print("Opcion no valida")
        opcion = int(input("Elige una opcion(1-4): "))
        seguir = True
    if opcion == 1:
        print("Haz elegido la opcion 1")
        agregar_producto(inventario)
        seguir = True
    elif opcion == 2:
        print("Haz elegido la opcion 2")
        ejecutar_venta(inventario)
        seguir = True
    elif opcion == 3:
        print("Haz elegido la opcion 3")
        mostrar_productos_disponibles(inventario)
        seguir = True
    else:
        print("Haz elegido la opcion 4. Haz salido del sistema.")
        seguir = False
    return seguir

seguir = True
while seguir == True:
    llamar_menu(MENU)
    seguir = ejecutar_opcion(seguir)
