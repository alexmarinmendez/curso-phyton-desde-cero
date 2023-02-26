from mock.datos_mock import profesores_mock
from utils.data_utils import profesores
from classes.profesor import Profesor
import time

def agregar():
    """Registra un profesor en la base de datos
    """
    print("\nRegistro de profesor nuevo...")
    nombres = input("Nombres (solo nombres): ")
    apellidos = input("Apellidos: ")
    dni = input("DNI: ")
    nacionalidad = input("Nacionalidad: ")
    cotizacion = float(input("Cotización /hora (USD): "))
    nuevo_profesor = Profesor(nombres, apellidos, dni, nacionalidad, cotizacion)
    profesores[dni] = nuevo_profesor
    print("Profesor registrado!\n")
    input("Press <ENTER> to continue...")

def eliminar():
    """Dar de baja un profesor. Cambia el atributo 'activo' a False para indicar que ya no se le asignará cursos
    """
    print("\nDar de baja un profesor...")
    dni = input("Ingrese DNI del profesor que desea DAR DE BAJA: ")
    profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, profesores[dni].cotizacion, profesores[dni].cant_horas, False)
    profesores[dni] = profesor
    print("BAJA registrada!\n")
    input("Press <ENTER> to continue...")

def editar():
    """Modifica 2 de los atributos del profesor. Solo es posible modificar la Cotización /hora y la Cantidad de horas de clases realizadas
    """
    print("\nModificando los datos de profesor...")
    dni = input("Ingrese DNI del profesor que desea modificar: ")
    print("Los datos del profesor seleccionado son:")
    print(profesores[dni])
    print("\nInformación que puede actualizar:")
    print("(1): Cotización /hora")
    print("(2): Cantidad de horas\n")
    clave_para_actualizar = int(input(("Qué información desea actualizar (1 o 2): ")))
    if (clave_para_actualizar == 1):
        dato_para_actualizar = float(input(f"Cuál es el nuevo valor para [Cotizacion /hora] (USD): "))
        profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, dato_para_actualizar, profesores[dni].cant_horas, profesores[dni].activo)
    else:
        dato_para_actualizar = int(input(f"Cuál es el nuevo valor para [Cantidad de horas]: "))
        profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, profesores[dni].cotizacion, dato_para_actualizar, profesores[dni].activo)
    profesores[dni] = profesor
    print("Dato actualizado!\n")
    input("Press <ENTER> to continue...")

def mostrar():
    """Imprime la lista de profesores registrados
    """
    print("\nLista de profesores...")
    for x,y  in profesores.items():
        print(x,y)
    print("Fin de la lista de profesores.\n")
    input("Press <ENTER> to continue...")

def buscar():
    """Imprime los datos de un profesor. Se busca por el DNI
    """
    print("\nBuscando profesor...")
    dni = input("Ingrese DNI del profesor que desea buscar: ")
    print("Profesor encontrado. Sus datos son:")
    print(profesores[dni])
    print("Fin de la lista de datos de este profesor.\n")
    input("Press <ENTER> to continue...")

def cargar_mock():
    """Añade datos de prueba (mock) a la base de datos (diccionario de profesores)
    """
    print("Cargando datos...")
    time.sleep(2)
    for x,y in profesores_mock.items():
        profesores[x]= Profesor(y['nombres'], y['apellidos'], y['dni'], y['nacionalidad'], y['cotizacion'])
    print("Se han cargado los datos!")
    input("Press <ENTER> to continue...")