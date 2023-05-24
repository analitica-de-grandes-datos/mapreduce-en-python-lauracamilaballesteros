#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = []
    for linea in sys.stdin:
        columnas = linea.split(",")
        if len(columnas) == 3:
            letter = columnas[0]
            fecha = columnas[1]
            valor = int(columnas[2])
            atributo.append([letter, fecha, valor])
    
    atributo_sort = sorted(atributo, key=lambda x: (x[0], x[2]))

    
    for elemento in atributo_sort:
        sys.stdout.write(f"{elemento[0]}   {elemento[1]}   {elemento[2]}\n") 