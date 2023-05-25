#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    dictionary = {}
    
    for line in sys.stdin:
        columns = line.split("\t")
        if len(columns) == 2:
            num = columns[0]
            letters = columns[1].strip()
            
            for letter in letters:
                if letter in dictionary:
                    dictionary[letter].append(num)
                else:
                    dictionary[letter] = [num]

    dictionary_sort = sorted(dictionary.items(), key=lambda x: x[0])
    
    for letter, values in dictionary_sort:
        values_str = ",".join(values)  
        sys.stdout.write(f"{letter}\t{values_str}\n")
        #