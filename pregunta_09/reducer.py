#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == "__main__":
    dictionary = {}
    count = 0
    
    for line in sys.stdin:
        columna = line.split(",")
        if len(columna) >= 3:
            letra = columna[0]
            date = columna[1]
            num = int(columna[2])
            
            if num in dictionary:
                if dictionary[num] > (letra, date):
                    dictionary[num] = (letra, date)
            else:
                dictionary[num] = (letra, date)
    
    dictionary_sort = sorted(dictionary.items())
    
    for num, (letter, date) in dictionary_sort:
        sys.stdout.write(f"{letter}   {date}   {num}\n")
        count += 1
        if count == 6:
            break
        #