import os


menu = """

1) Apagar monitor portatil
2) Apagat monitor adicional
3) Listar monitores 
4) Salir

"""

while true:
    os.system("clear")
    print(menu)
    opt = input("Ingrese una opcion: ")
    if (opt == "1"):
