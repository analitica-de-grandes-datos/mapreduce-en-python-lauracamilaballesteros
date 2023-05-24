#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for linea in sys.stdin:
        columnas = linea.split(",")
        if len(columnas) == 2:
            letter = columnas[0]
            amount = float(columnas[1])
            if letter in atributo:
                atributo[letter] = {
                    'max': max(atributo[letter]['max'], amount),
                    'min': min(atributo[letter]['min'], amount)
                }
            else:
                atributo[letter] = {'max': amount, 'min': amount}
    
    atributo_sort = sorted(atributo.items(), key=lambda x: x[0])
    for atributo, valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor['max']}\t{valor['min']}\n")