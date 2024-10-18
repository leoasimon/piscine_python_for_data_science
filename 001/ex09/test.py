import ft_package


def main():
    print('Let\'s throw a dice...')
    result = ft_package.throw_dice()
    print(f'that\'s a {result}')

    deck = ft_package.get_52_deck()
    print('Now let\'s pick a card')
    card = ft_package.pick_random(deck)
    print(f'You picked {card}')


if __name__ == '__main__':
    main()
