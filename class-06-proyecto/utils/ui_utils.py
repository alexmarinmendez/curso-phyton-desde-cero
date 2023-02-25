from utils.crud_utils import agregar, eliminar, editar, mostrar, cargar_mock, buscar

def mostrar_diccionario(diccionario: dict):
    """Imprime el menú de opciones en consola

    Args:
        diccionario (dict): Diccionario con el menú de opciones
    """
    for x, y in diccionario.items():
        print(f"  [{x}]: --> {y}")
    print("\n++++++++++++++++++++++++++++++++++++++++++")

def comprobar_opcion(opcion):
    if opcion>=1 and opcion<=8:
        if opcion == 1:
            agregar()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            editar()
        elif opcion == 4:
            mostrar()
        elif opcion == 5:
            cargar_mock()
        elif opcion == 6:
            buscar()
        elif opcion == 7:
            pass
    else:
        print("\nOpción incorrecta. Se espera un número entre 1 y 8\n")

