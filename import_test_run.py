from import_test import x, y

print('from import_test import x, y >> x, y:', x, y)
x = 100
y[1] = 500
print('x, y:', x, y)

import import_test
print('import import_test >> import_test.x, import_test.y:', import_test.x, import_test.y)