#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for linea in sys.stdin:
        columnas = linea.split("\n")
        columna_credit = columnas[0]
        if columna_credit in atributo:
            atributo[columna_credit] += 1
        else:
            atributo[columna_credit] =1
    atributo_sort = sorted(atributo.items())
    for atributo,valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")