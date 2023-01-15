# Pedirle al usuario que ingrese 2 número enteros y que devuelva la suma, la multiplicación
# la resta y division

# una pequeña ayuda
numero_a = int(input("Ingrese un número entero: "))
numero_b = int(input("Ingrese otro número entero: "))

suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = round(numero_a / numero_b, 2)

print(f"La suma de ambos números es: {suma}")
print(f"La resta de ambos números es: {resta}")
print(f"La multiplicacion de ambos números es: {multiplicacion}")
print(f"La division de ambos números es: {division}")

