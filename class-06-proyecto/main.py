from os import system
from utils.ui_utils import mostrar_diccionario, comprobar_opcion
from mock.menu import menu

verificacion = False
while not verificacion:
    system("cls")
    print("\n++++++++++++++++++++++++++++++++++++++++++")
    print("+       ALEZHIA Online C0D3R SCH00L      +")
    print("++++++++++++++++++++++++++++++++++++++++++\n")
    mostrar_diccionario(menu)
    valor = int(input("\nElija una opción: "))
    comprobar_opcion(valor)
    verificacion = (valor == 8)