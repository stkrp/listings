"""
Повторение списка (умножение списка на число)
"""

from copy import deepcopy


def test_var_init():
    """ Инициализация тестовых переменных """
    global dct, lst
    dct = {'a': [1], 'b': 2, 'c': '3'}
    lst = [9, 99, 999]


test_var_init()

m_lst_1 = [dct, lst] * 2
m_lst_2 = [dct] * 2
m_lst_3 = [lst] * 2

dct['d'] = (4,)
lst.append(9999)

m_lst_1[0]['e'] = {5: None}
m_lst_2[0]['f'] = [6]
m_lst_3[0].append(99999)

print(m_lst_1, m_lst_2, m_lst_3, dct, lst, sep='\n')

# Полное копирование не решает проблемы
test_var_init()
m_lst_4 = [deepcopy(dct)] * 2
dct['g'] = 7
print(m_lst_4)
m_lst_4[0]['h'] = '8'
print(m_lst_4)

# Использование только генератора списка тоже не помогает
test_var_init()
m_lst_5 = [dct for i in range(2)]
dct['i'] = (9,)
print(m_lst_5)

# Комбинирование deepcopy и генератора списка решает проблему
test_var_init()
m_lst_6 = [deepcopy(dct) for i in range(2)]
dct['j'] = {10: None}
m_lst_6[0]['k'] = [11]
print(m_lst_6)

m_lst_7 = [[] for i in range(2)]
m_lst_7[0].append(True)
print(m_lst_7)