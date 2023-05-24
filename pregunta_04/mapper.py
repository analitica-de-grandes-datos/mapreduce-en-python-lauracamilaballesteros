#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split(" ")
        columna_letter = columnas[0]
        sys.stdout.write(f"{columna_letter}\n")

