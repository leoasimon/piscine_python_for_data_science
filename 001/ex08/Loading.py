def get_bar_c(i, progress, bar_width):
    if i >= progress:
        return ' '
    return '='


def get_progress_bar(i, n_elems) -> str:
    bar_width = 30
    progress = round(i / n_elems * bar_width)
    core_arr = [get_bar_c(i, progress, bar_width) for i in range(bar_width)]
    # return f'|{''.join(cor_arr)}|'
    return ''.join(core_arr)


def get_percent(i, n_elems) -> str:
    return f'{round(i / n_elems * 100)}%'


def get_progress(i, n_elems) -> str:
    return f'{i}/{n_elems}'


def ft_tqdm(lst: range) -> None:
    n_elems = len(lst)
    for el in lst:
        percent = get_percent(el, n_elems)
        progress = get_progress(el + 1, n_elems)
        bar = get_progress_bar(el, n_elems)
        print(f'{percent}|{bar}| {progress}', end='\r')
        yield
    return 1
