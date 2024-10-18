from ft_filter import ft_filter


def ft_filter_tests():
    def is_odd(n):
        return n % 2 != 0

    items = [0, 1, 2, 3, 4, 5]
    expected = list(filter(is_odd, items))
    actual = ft_filter(is_odd, items)

    assert expected == actual


if __name__ == '__main__':
    ft_filter_tests()
