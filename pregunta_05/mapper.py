#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split("   ")
        fecha_texto = columnas[1]
        fecha = fecha_texto.split("-")
        mes = fecha[1]
        sys.stdout.write(f"{mes}\n")
        
        
        #cat data.csv | python3 mapper.py | sort | python3 reducer.py