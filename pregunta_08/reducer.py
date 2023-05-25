#
# >>> Escriba el codigo del reducer a partir de este punto <<<

import sys

if __name__ == "__main__":
    dictionary = {}
    for line in sys.stdin:
        columns = line.split(",")
        if len(columns) == 2:
            letter = columns[0]
            amount = float(columns[1])
            if letter in dictionary:
                dictionary[letter][0] += amount
                dictionary[letter][1] += 1
            else:
                dictionary[letter] = [amount, 1]
    
    dictionary_sort = sorted(dictionary.items(), key=lambda x: x[0])
    for atributo, valores in dictionary_sort:
        suma = valores[0]
        contador = valores[1]
        promedio = suma / contador
        sys.stdout.write(f"{atributo}\t{suma}\t{promedio}\n")

