#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for linea in sys.stdin:
        columnas = linea.split("\t")
        if len(columnas) == 2:
            columna1 = columnas[0] 
            columna2 = int(columnas[1])
            atributo[columna1] = columna2
            
    atributo_sort = sorted(atributo.items(), key=lambda x: x[1])
    for atributo,valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")
        