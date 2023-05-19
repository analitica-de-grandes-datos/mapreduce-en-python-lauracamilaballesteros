#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split(",")
        if len(columnas) == 2:
            columna1 = columnas[0]
            columna2 = columnas[1]
        sys.stdout.write(f"{columna1}\t{columna2}\n")
        