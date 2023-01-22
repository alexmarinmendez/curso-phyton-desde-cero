menu = {
    1: "Agregar nuevo contacto",
    2: "Eliminar contacto",
    3: "Editar contacto",
    4: "Ver todos los contactos",
    5: "Buscar un contacto",
    6: "Salir"
}

def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(f"{x}: {y}")

mostrar_diccionario(menu)