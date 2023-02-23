from persona import Persona

class Programador(Persona):
    def __init__(self, nombres: str, apellidos: str, dni: str, nacionalidad: str, stack: str, seniority: str):
        # super().__init__(nombres, apellidos, dni, nacionalidad)
        Persona().__init__(self, nombres, apellidos, dni, nacionalidad)
        self.stack = stack
        self.seniority = seniority
        
    def __str__(self):
        return f"Resumen de la Clase Programador:\n \
                Nombres: {self.nombres}\n \
                Apellidos: {self.apellidos}\n \
                DNI: {self.dni}\n \
                Nacionalidad: {self.nacionalidad}\n \
                Stack de especialidad: {self.stack}\n \
                Experiencia: {self.seniority}\n"

if (__name__ == "__main__"):
    print("Módulo programador")
    
    programador = Programador("Alex", "Marin Mendez", "18205786", "Marciana", "Javascript", "Jr")
    print(programador)