"""
Расширить передаваемый список набором элементов, добавляя эти элементы в начало списка.
Передаваемый список изменяется во всех функциях.
"""


def front_extend_list_only_sum(items_lst, lst):
    """
    :param items_lst: list
    """
    lst = items_lst + lst


def front_extend_sum(items, lst):
    """
    :param items: iter
    """
    lst = list(items) + lst


def front_extend_slice(items, lst):
    """
    :param items: iter
    """
    lst[0:0] = items


if __name__ == '__main__':
    import time

    replays = 100000
    funcs = (front_extend_list_only_sum, front_extend_sum, front_extend_slice)

    results = {}
    replays_params = {
        func.__name__: (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i']),
        ) * replays
        for func in funcs
    }

    for func in funcs:
        results[func.__name__] = {
            'duration': 0,
            'avg_duration': 0,
            'replays': replays,
            'replays_duration': []
        }
        for replay in range(replays):
            params = replays_params[func.__name__][replay]
            start = time.clock()
            func(*params)
            end = time.clock()
            results[func.__name__]['replays_duration'].append(end - start)

        results[func.__name__]['duration'] = sum(results[func.__name__]['replays_duration'])
        results[func.__name__]['avg_duration'] = results[func.__name__]['duration'] / results[func.__name__]['replays']

        # DEBUG
        del results[func.__name__]['replays_duration']

    print(results)