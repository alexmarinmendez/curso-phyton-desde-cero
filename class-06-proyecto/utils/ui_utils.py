def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(f"  [{x}]: --> {y}")
    print("\n++++++++++++++++++++++++++++++++++++++++++")

def comprobar_opcion(opcion):
    if opcion>=1 and opcion<=7:
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
    else:
        print("\nOpción incorrecta. Se espera un número entre 1 y 7\n")

