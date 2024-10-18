import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. "
}


def main():
    args = sys.argv[1:]
    # todo: accept stdin

    s = args[0].upper()
    code = [NESTED_MORSE.get(c, '?') for c in s]
    if '?' in code:
        print('AssertionError: the arguments are bad')
        return 1
    print(' '.join(code).strip())
    return 0


if __name__ == '__main__':
    main()
