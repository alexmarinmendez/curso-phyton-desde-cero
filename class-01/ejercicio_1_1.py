# Completa el código

"""
Para este ejercicio se pide que completes y corrijas el código para que funcione
Deberás mostrar en la consola 
Nombre
Apellido
Edad
Año de nacimiento
Si es mayor de edad
"""

# Entrada de datos:

nombre = input("Ingresá tu nombre: ")
#apellido
apellido = input("Ingresá tu apellido: ")
edad = int(input("Ingresá tu edad: "))

# Procesando los datos:

anio_nacimiento = 2023 - edad

es_mayor = 18 < edad

# Salida de datos

print(f'Su nombre es: {nombre}')
print(f"Su apellido es: {apellido}")
print(f"Su edad es: {edad}")
print(f"Su año de nacimiento es: {anio_nacimiento}")