# from persona import Persona
from classes.persona import Persona

class Profesor(Persona):
    """Clase hija Profesor

    Args:
        nombres: str
        apellidos: str
        dni: str
        nacionalidad: str
        cotizacion: float (Cotización en USD por cada hora de clase realizada)
        cant_horas: int (Opcional) Cantidad de horas de clase realizadas. Valor por defecto: 0
        activo: bool (Opcional) Indica si está activo para asignarle cursos o no. Valor por defecto: True
    """
    def __init__(self, nombres: str, apellidos: str, dni: str, nacionalidad: str, cotizacion: float, cant_horas = 0, activo = True):
        super().__init__(nombres, apellidos, dni, nacionalidad)
        self.cotizacion = cotizacion
        self.cant_horas = cant_horas
        self.activo = activo
        
    def __str__(self):
        return f" \
                Nombres: {self.nombres}\n \
                Apellidos: {self.apellidos}\n \
                DNI: {self.dni}\n \
                Nacionalidad: {self.nacionalidad}\n \
                Contizacion /hora: USD {self.cotizacion}\n \
                Cant. de horas trabajadas: {self.cant_horas}\n \
                Estado: {self.activo}\n"
    
if __name__ == "__main__":
    print("Módulo profesor")
    
    profesor = Profesor("Alex", "Marin Mendez", "18205786", "Peruana", 41.50)
    ver = profesor
    print(ver.datos_dict())

