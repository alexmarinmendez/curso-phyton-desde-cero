from persona import Persona

class Profesor(Persona):
    def __init__(self, nombres: str, apellidos: str, dni: str, nacionalidad: str, cotizacion: float, cant_horas: int):
        super().__init__(nombres, apellidos, dni, nacionalidad)
        self.cotizacion = cotizacion
        self.cant_horas = cant_horas
        
    def __str__(self):
        return f"Resumen de la Clase Profesor:\n \
                Nombres: {self.nombres}\n \
                Apellidos: {self.apellidos}\n \
                DNI: {self.dni}\n \
                Nacionalidad: {self.nacionalidad}\n \
                Contizacion /hora: USD {self.cotizacion}\n \
                Cant. de horas trabajadas: {self.cant_horas}\n"

if (__name__ == "__main__"):
    print("Módulo profesor")
    
    profesor = Profesor("Alex", "Marin Mendez", "18205786", "Marciana", 41.50, 16)
    print(profesor)