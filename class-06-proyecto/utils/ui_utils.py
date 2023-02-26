from utils.crud_utils import ProfesorManager

class UI:
    def mostrar_diccionario(self, diccionario: dict):
        """Imprime el menú de opciones en consola

        Args:
            diccionario (dict): Diccionario con el menú de opciones
        """
        for x, y in diccionario.items():
            print(f"  [{x}]: --> {y}")
        print("\n++++++++++++++++++++++++++++++++++++++++++")

    def comprobar_opcion(self, opcion):
        if opcion>=1 and opcion<=8:
            profeManager = ProfesorManager()
            if opcion == 1:
                profeManager.agregar()
            elif opcion == 2:
                profeManager.eliminar()
            elif opcion == 3:
                profeManager.editar()
            elif opcion == 4:
                profeManager.mostrar()
            elif opcion == 5:
                profeManager.cargar_mock()
            elif opcion == 6:
                profeManager.buscar()
            elif opcion == 7:
                pass
        else:
            print("\nOpción incorrecta. Se espera un número entre 1 y 8\n")

