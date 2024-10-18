import sys


def is_punctuation(c: str) -> bool:
    punctuation_marks = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
        '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
        '}', '~'
    ]

    # Additional punctuation marks
    additional_punctuation = [
        '«', '»', '–', '—', '‘', '’', '“', '”', '…',
        '‽', '¡', '¿', '‹', '›'
    ]

    # Combine the two lists
    all_punctuation = punctuation_marks + additional_punctuation

    return c in all_punctuation


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('What is the text to count?')
        s = sys.stdin.readline()
    else:
        s = args[0]

    total = len(s)
    lowers = 0
    uppers = 0
    punctuations = 0
    spaces = 0
    digits = 0

    for c in s:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif is_punctuation(c):
            punctuations += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digits += 1

    print(f'The text contains {total} characters:')
    print(f'{uppers} upper letters')
    print(f'{lowers} lower letters')
    print(f'{punctuations} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')


if __name__ == '__main__':
    main()
