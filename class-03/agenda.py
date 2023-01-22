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
    print("\n****************************")
    print("*    AGENDA DE CONTACTOS   *")
    print("****************************")
    for x, y in diccionario.items():
        print(f"{x}: {y}")
    print("****************************")

def comprobar_opcion(opcion):
    if opcion>=1 and opcion<=6:
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            eliminar_contacto()
        elif opcion == 3:
            editar_contacto()
        elif opcion == 4:
            mostrar_contactos()
        elif opcion == 5:
            buscar_contacto()
    else:
        print("\nOpción incorrecta. Se espera un número entre 1 y 6\n")

def agregar_contacto():
    print("\nAgregando un nuevo contacto...")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Número de teléfono: ")
    contactos[nombre] = {'Direccion': direccion, 'Telefono': telefono}
    print("Contacto guardado!\n")

def eliminar_contacto():
    print("\nEliminando un contacto...")
    nombre = input("Ingrese nombre del contacto que desea eliminar: ")
    contactos.pop(nombre)
    print("Contacto eliminado!\n")

def editar_contacto():
    print("\nModificando los datos de un contacto...")
    nombre = input("Ingrese nombre del contacto que desea modificar: ")
    print("Los datos del contacto seleccionado son:")
    print(contactos[nombre])
    clave_para_actualizar = input(("Qué información desea actualizar: "))
    dato_para_actualizar = input(f"Cuál es el nuevo valor para '{clave_para_actualizar}': ")
    contactos[nombre][clave_para_actualizar] = dato_para_actualizar
    print("Dato actualizado!\n")

def mostrar_contactos():
    print("\nMostrando contactos...")
    print(contactos)
    print("Fin de la lista de contactos.\n")

def buscar_contacto():
    print("\nBuscando contacto...")
    nombre = input("Ingrese nombre del contacto que desea buscar: ")
    print("Contacto encontrado. Sus datos son:")
    print(contactos[nombre])
    print("Fin de la lista de datos de este contacto.\n")


verificacion = False
while not verificacion:
    mostrar_diccionario(menu)
    valor = int(input("Elija una opción: "))
    comprobar_opcion(valor)
    verificacion = (valor == 6)