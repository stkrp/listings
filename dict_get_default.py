"""
Изменяемый объект как значение по умолчанию метода словаря get.
"""

dct = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900, 10: [1, 2, 3, 4, 5]}
default = {5: 1, 55: 2}

# Создание объекта значения по умолчанию в вызове get
tmp = []
for i in (11, 12):
    tmp.append(dct.get(i, {9: 1, 99: 2, 999: 3}))
b, c = tmp

# Использование заранее инициализированной переменной в качестве значения по умолчанию в вызове get
tmp = []
for i in (11, 12):
    tmp.append(dct.get(i, default))
d, e = tmp

print(
    'b: {}'.format(b), 'c: {}'.format(c), 'd: {}'.format(d), 'e: {}'.format(e),
    'default: {}'.format(default),
    sep='\n'
)

b[9] = 10
c[99] = 100
d[5] = -1
d[55] = -2
d[555] = -3

print(
    'upd b: {}'.format(b), 'upd c: {}'.format(c), 'upd d: {}'.format(d), 'upd e: {}'.format(e),
    'default: {}'.format(default),
    sep='\n'
)