#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        columns = line.split("\t")
        num = columns[0]
        letters = columns[1].strip().split(",")
        for letter in letters:
            sys.stdout.write(f"{num}\t{letter}\n")
         #cat data.csv | python3 mapper.py | sort | python3 reducer.py