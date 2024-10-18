from time import sleep
from tqdm import tqdm


def main():
    for elem in tqdm(range(333)):
        sleep(0.005)
        print()


if __name__ == '__main__':
    main()
