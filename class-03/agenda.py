menu = {
    1: "Agregar nuevo contacto",
    2: "Eliminar contacto",
    3: "Editar contacto",
    4: "Ver todos los contactos",
    5: "Buscar un contacto",
    6: "Salir"
}
contactos = {}

def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(f"{x}: {y}")

def comprobar_opcion(opcion):
    if opcion>=1 and opcion<=6:
        if opcion == 1:
            agregar_contacto()
        elif opcion == 4:
            mostrar_contactos()
    else:
        print("\nOpción incorrecta. Se espera un número entre 1 y 6\n")

def agregar_contacto():
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Número de teléfono: ")
    contactos[nombre] = {'Direccion': direccion, 'Telefono': telefono}
    print("Contacto guardado!")

def mostrar_contactos():
    print(contactos)

verificacion = False
while not verificacion:
    mostrar_diccionario(menu)
    valor = int(input("Elija una opción: "))
    comprobar_opcion(valor)
    verificacion = (valor == 6)