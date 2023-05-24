#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for linea in sys.stdin:
        columnas = linea.split("\n")
        mes = columnas[0]
        if mes in atributo:
            atributo[mes] += 1
        else:
            atributo[mes] = 1
    atributo_sort = sorted(atributo.items())
    for atributo,valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")
        