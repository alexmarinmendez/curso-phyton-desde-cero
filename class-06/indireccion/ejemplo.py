# https://es.stackoverflow.com/questions/457234/que-es-la-indireccion-en-herencia-multiple-en-python
class Persona:
  def __init__(self, nombre, apellido, edad, sexo):
    print("Inicializando Persona")
    self.nombre = nombre
    self.apellido = apellido
    self.sexo = sexo
    self.edad = edad

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, sexo, salario):
    print("Inicializando Empleado")
    super().__init__(nombre, apellido, edad, sexo)
    self.salario = salario

class InteligenciaArtificial(Persona):
  def __init__(self, nombre, apellido, edad, sexo):
    print("Inicializando InteligenciaArtificial")
    super().__init__(nombre, apellido, edad=None, sexo=None)
    self.is_a_bot = True

class EmpleadoAI(Empleado, InteligenciaArtificial):
  pass

e = EmpleadoAI("Cortana", "Microsoft", edad=100, sexo="Femenino", salario=2000)
# e = EmpleadoAI("Cortana", "Microsoft", edad=None, sexo=None, salario=2000)
print(e)
print(vars(e))