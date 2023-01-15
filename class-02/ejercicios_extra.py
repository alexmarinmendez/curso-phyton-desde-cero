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

# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota>
# donde <asignatura> es cada una des las asignaturas de la lista
# y <nota> cada una de las correspondientes notas introducidas por el usuario.

scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "? ")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])