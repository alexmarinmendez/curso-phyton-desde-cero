def agregar():
    print("\Registro de profesor nuevo...")
    nombre = input("Nombre del profesor: ")
    precio = float(input("Precio: "))
    cantidad = float(input("Cantidad: "))
    productos[nombre] = {'Precio': precio, 'Cantidad': cantidad}
    print("Profesor registrado!\n")
