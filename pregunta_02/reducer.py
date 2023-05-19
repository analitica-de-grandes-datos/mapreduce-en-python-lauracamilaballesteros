#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for linea in sys.stdin:
        columnas = linea.split("\t")
        purpose = columnas[0]
        amount = int(columnas[1])
        if purpose in atributo:
            atributo[purpose] = max(atributo[purpose],amount)
        else:
            atributo[purpose] = amount
    atributo_sort = sorted(atributo.items())
    for atributo,valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")
        