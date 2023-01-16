""" Usando el formulario creado en la primera clase """

nombre = input("Cual es su nombre? ")
apellido = input("Cual es su apellido? ")
edad = input("Cual es su edad: ")

# 1- Crear una lista con esos datos y mostrar por consola 
lista = [nombre, apellido, edad]
print(f'La lista de datos es {lista}')

# 2- Crear un diccionario poniendo como clave lo que represeta cada valor
diccionario = {
    'nombre': nombre,
    'apellido': apellido,
    'edad' : edad
}
print(f'El diccionario de datos es {diccionario}')

# 3- Solicitar al usuario ingresar 3 datos por consola y luego insertarlos en un conjunto 
# para mostrarlos por pantalla
# conjunto = {nombre, apellido, edad}
conjunto = set(lista)
print(f'El conjunto de datos es {conjunto}')



print('=========================================================')
""" DICCIONARIOS ANIDADOS """

# 4- Introducir en un diccionario 4 alumnos, cada uno tendrá 3 notas de las siguientes asignaturas
# Lengua - Matemática - Informática

alumno_1 = {
    'Lengua': 9,
    'Matemática': 7,
    'Informática': 7
}

alumno_2 = {
    'Lengua': 3,
    'Matemática': 4,
    'Informática': 5
}


alumnos = {
}

# Dos Maneras de agregar datos a un diccionario
alumnos['alumno_1'] = alumno_1
alumnos.update({'alumno_2': alumno_2})

# print(alumnos) # {'alumno_1': {'Lengua': 9, 'Matemática': 7, 'Informática': 7}, 'alumno_2': {'Lengua': 3, 'Matemática': 4, 'Informática': 5}}

alumno_3 = {
    'Lengua': 9,
    'Matemática': 5,
    'Informática': 6
}

alumno_4 = {
    'Lengua': 4,
    'Matemática': 9,
    'Informática': 10
}

alumnos['alumno_3'] = alumno_3
alumnos['alumno_4'] = alumno_4
print(alumnos)
# 5- Actualiza los datos de un alumno en particular y elimina uno del diccionario 
# "alumnos" que precisamente no haya sido el que se actualizaron los datos
alumno_4['Lengua'] = 6
print(alumnos)
alumnos.pop('alumno_3')
print(alumnos)

# 6- Agrega un alumno más por consola, solamente pidiendo que ingrese las notas de este quinto alumno  
lengua_5 = input('Nota de Lengua del alumno extra: ')
matematica_5 = input('Nota de Matemática del alumno extra: ')
informatica_5 = input('Nota de Informática del alumno extra: ')
alumno_5 = {}
alumno_5['Lengua'] = lengua_5
alumno_5['Matemática'] = matematica_5
alumno_5['Informática'] = informatica_5
alumnos.update({'alumno_5': alumno_5})
print(alumnos)