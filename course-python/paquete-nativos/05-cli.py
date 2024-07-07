import sys
from pathlib import Path
import os
print(sys.argv)  # Argumento al script que le estamos pasando


def cli(args):
    if len(args) == 1:
        print("No se pasoron argumentos")
    if len(args) != 3:
        print("Se necesitan dos argumentos")

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print('origen no exite')

    destino = args[2]
    d = Path(destino)
    if d.exists():

        os.rename(str(origen), str(destino))
        print("Archivo renomabrodo con exito!")


cli(sys.argv)
