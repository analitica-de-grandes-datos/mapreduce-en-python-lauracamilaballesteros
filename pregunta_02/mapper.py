#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split(",")
        columna_purpose = columnas[3]
        columna_amount = columnas[4]
        sys.stdout.write(f"{columna_purpose}\t{columna_amount}\n")
        