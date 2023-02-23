import os
from profesor import Profesor
from programador import Programador

class ProfesorProgramacion(Profesor, Programador):
    def __init__(
                self, 
                nombres: str, 
                apellidos: str, 
                dni: str, 
                nacionalidad: str, 
                cotizacion: float, 
                cant_horas: int, 
                stack: str, 
                seniority: str,
                f_ingreso: str
        ):
        Profesor.__init__(self, nombres, apellidos, dni, nacionalidad, cotizacion, cant_horas)
        Programador.__init__(self, nombres, apellidos, dni, nacionalidad, stack, seniority)
        self.f_ingreso = f_ingreso
        
    def __str__(self):
        return f"Resumen de la Clase ProfesorProgramacion:\n \
                Nombres: {self.nombres}\n \
                Apellidos: {self.apellidos}\n \
                DNI: {self.dni}\n \
                Nacionalidad: {self.nacionalidad}\n \
                Contizacion /hora: USD {self.cotizacion}\n \
                Cant. de horas trabajadas: {self.cant_horas}\n \
                Stack de especialidad: {self.stack}\n \
                Experiencia: {self.seniority}\n"

if (__name__ == "__main__"):
    os.system('cls')
    print("Módulo profesor_programacion")
        
    profesor_programacion = ProfesorProgramacion("Alex", "Marin Mendez", "18205786", "Marciana", cotizacion=51.2, cant_horas=23, stack="Javascript", seniority="Jr", f_ingreso="hoy")
    print(profesor_programacion)