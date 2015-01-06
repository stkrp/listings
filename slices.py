"""
Приемы, основанные на применении срезов
"""

# Срезы [0:x] равносильны [:x], но в коде используются [0:x] для наглядности

EXAMPLE_LIST = [1, 2, 3, 'a', 'b', 'c']


def shallow_copy(lst):
    return lst[:]


def add_item_to_the_top(item, lst):
    """ Добавить элемент в начало списка. Изменяет передаваемый список. """
    lst[0:0] = (item,)


def front_extend(items, lst):
    """ Расширить передаваемый список набором элементов, добавляя эти элементы в начало списка. """
    lst[0:0] = items


def delete_first_item(lst):
    """ Удалить первый элемент списка. Изменяет передаваемый список. """
    lst[0:1] = []


def delete_from_to(p_from, p_to, lst):
    """ Удалить подпоследовательность. Последний элемент (p_to) не удаляется """
    lst[p_from:p_to] = []


if __name__ == '__main__':
    sh_copy = shallow_copy(EXAMPLE_LIST)
    sh_copy[1] = 4
    print('original', EXAMPLE_LIST, '\nnew', sh_copy)

    add_item_to_the_top(0, sh_copy)
    print('updated', sh_copy)

    front_extend('zxc', sh_copy)
    print('front_extend 1', sh_copy)
    front_extend(('zxc',), sh_copy)
    print('front_extend 2', sh_copy)

    delete_first_item(sh_copy)
    print('delete_first_item', sh_copy)

    delete_from_to(3, 6, sh_copy)
    print('delete_from_to', sh_copy)