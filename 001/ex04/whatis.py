import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        return
    if len(args) > 1:
        print('AssertionError: more than one argument is provided')
        return

    try:
        n = int(args[0])
    except:
        print("AssertionError: argument is not an integer")
        return

    if n % 2 == 0:
        print('I\'m Even.')
    else:
        print('I\'m Odd.')

if __name__ == '__main__':
    main()
