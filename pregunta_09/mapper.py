#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split("   ")
        letra = columnas[0]
        fecha = columnas[1]
        valor = columnas[2]
        sys.stdout.write(f"{letra},{fecha},{valor}\n")
        
        
        #cat data.csv | python3 mapper.py | sort | python3 reducer.py