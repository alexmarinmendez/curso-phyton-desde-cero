# Tomado de https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la lista.

for subject in subjects:
    print("Yo estudio " + subject)