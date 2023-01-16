""" Usando el formulario creado en la primera clase """


# 1- Crear una lista con esos datos y mostrar por consola 

# 2- Crear un diccionario poniendo como clave lo que represeta cada valor

# 3- Solicitar al usuario ingresar 3 datos por consola y luego insertarlos en un conjunto 
# para mostrarlos por pantalla

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

print(alumnos) # {'alumno_1': {'Lengua': 9, 'Matemática': 7, 'Informática': 7}, 'alumno_2': {'Lengua': 3, 'Matemática': 4, 'Informática': 5}}

# alumno_3 

# alumno_4 

# 5- Actualiza los datos de un alumno en particular y elimina uno del diccionario 
# "alumnos" que precisamente no haya sido el que se actualizaron los datos

# 6- Agrega un alumno más por consola, solamente pidiendo que ingrese las notas de este quinto alumno  