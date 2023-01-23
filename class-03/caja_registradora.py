menu = {
    1: "Agregar producto",
    2: "Eliminar producto",
    3: "Editar producto",
    4: "Ver todos los producto",
    5: "Buscar un producto",
    6: "Mostrar resumen de compra",
    7: "Salir"
}
productos = {
    'Pan': {'Precio': 0.2, 'Cantidad': 4.0},
    'Huevos': {'Precio': 1.6, 'Cantidad': 6.0},
    'Mantequilla': {'Precio': 1.8, 'Cantidad': 1.0}
    }

def mostrar_diccionario(diccionario: dict):
    print("\n****************************")
    print("*    CAJA REGISTRADORA     *")
    print("****************************")
    for x, y in diccionario.items():
        print(f"{x}: {y}")
    print("****************************")

def comprobar_opcion(opcion):
    if opcion>=1 and opcion<=7:
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            editar_producto()
        elif opcion == 4:
            mostrar_productos()
        elif opcion == 5:
            buscar_producto()
        elif opcion == 6:
            mostrar_resumen()
    else:
        print("\nOpción incorrecta. Se espera un número entre 1 y 7\n")

def agregar_producto():
    print("\nAgregando un nuevo producto a la compra...")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = float(input("Cantidad: "))
    productos[nombre] = {'Precio': precio, 'Cantidad': cantidad}
    print("Producto registrado!\n")

def eliminar_producto():
    print("\nEliminando un producto...")
    nombre = input("Ingrese nombre del producto que desea eliminar: ")
    productos.pop(nombre)
    print("Producto eliminado!\n")

def editar_producto():
    print("\nModificando los datos de un producto...")
    nombre = input("Ingrese nombre del producto que desea modificar: ")
    print("Los datos del producto seleccionado son:")
    print(productos[nombre])
    clave_para_actualizar = input(("Qué información desea actualizar: "))
    dato_para_actualizar = float(input(f"Cuál es el nuevo valor para '{clave_para_actualizar}': "))
    productos[nombre][clave_para_actualizar] = dato_para_actualizar
    print("Producto actualizado!\n")

def mostrar_productos():
    print("\nMostrando productos...")
    print(productos)
    print("Fin de la lista de productos.\n")

def buscar_producto():
    print("\nBuscando producto...")
    nombre = input("Ingrese nombre del producto que desea buscar: ")
    print("Producto encontrado. Sus datos son:")
    print(productos[nombre])
    print("Fin de la lista de datos de este producto.\n")

def mostrar_resumen():
    print("\nResúmen de su compra...")
    print("Productos registrados en su órden de compra")
    print("-----------------------------------------------------")
    # Intento de dar formato a la tabla resumen
    # for x, y in productos.items():
    #     for a, b in productos[x].items():
    #         print(f"{a}: {b}")
    total = 0
    for x, y in productos.items():
        subtotal = 1
        for a, b in productos[x].items():
            subtotal *= productos[x][a]
        total += subtotal
        print(f"{x}:\t{y}\t")
        print("Subtotal: {0:.2f}".format(subtotal))
    print("-----------------------------------------------------")
    print(f"Cantidad de productos registrados: {len(productos)}")
    print("Total de dinero a pagar: {0:.2f}".format(total))


verificacion = False
while not verificacion:
    mostrar_diccionario(menu)
    valor = int(input("Elija una opción: "))
    comprobar_opcion(valor)
    verificacion = (valor == 7)