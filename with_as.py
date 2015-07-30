"""
Пример реализации объекта с поддержкой контекстного менеджера with as
Для демонстрации разработаны 5 классов:
* ContextManagerEnterResult - объект, возвращаемый методом __enter__
* _ContextManagerObjectBase - объект с поддержкой контекстного менеджера (базовый)
* ContextManagerObjectInterceptException - объект с поддержкой контекстного менеджера, перехватывающего ошибку
* ContextManagerObjectNotInterceptException - объект с поддержкой контекстного менеджера, не перехватывающего ошибку
* ContextManagerOwner - возвращает объект с поддержкой конекстного менеджера
"""


class ContextManagerEnterResult(object):
    """ Результат вызова метода __enter__ """
    def __init__(self, msg, exception=None):
        self.msg = msg
        self.exception = exception

    def upper(self):
        return self.msg.upper()

    def lower(self):
        return self.msg.lower()

    def raise_exception(self):
        if self.exception is not None:
            raise self.exception
        else:
            print('Exception is None')


class _ContextManagerObjectBase(object):
    """ Объект с поддержкой менеджера контекста """
    def __init__(self, msg, exception=None):
        self.msg = msg
        self.exception = exception

    def __enter__(self):
        print('Enter!')
        return ContextManagerEnterResult(self.msg, self.exception)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit!')
        if exc_type is not None:
            print('exc_type: {} | exc_val: {} | exc_tb: {}'.format(exc_type, exc_val, exc_tb))
        print()


class ContextManagerObjectInterceptException(_ContextManagerObjectBase):
    """ Объект с поддержкой менеджера контекста, перехватывающего ошибку """
    def __exit__(self, exc_type, exc_val, exc_tb):
        _ContextManagerObjectBase.__exit__(self, exc_type, exc_val, exc_tb)
        return True


class ContextManagerObjectNotInterceptException(_ContextManagerObjectBase):
    """ Объект с поддержкой менеджера контекста, не перехватывающего ошибку """
    def __exit__(self, exc_type, exc_val, exc_tb):
        _ContextManagerObjectBase.__exit__(self, exc_type, exc_val, exc_tb)
        return


class ContextManagerCaller(object):
    """
    Вызывает методы, возвращающие объекты с поддержкой менеджера контекста:
    * context_manager_intercept - не возбуждает исключение при выходе, если оно возникло
    * context_manager_not_intercept - возбуждает исключение при выходе, если оно возникло
    """
    def __init__(self, msg):
        self.msg = msg

    def context_manager_intercept(self, exception=None):
        return ContextManagerObjectInterceptException(self.msg, exception)

    def context_manager_not_intercept(self, exception=None):
        return ContextManagerObjectNotInterceptException(self.msg, exception)

if __name__ == '__main__':
    caller = ContextManagerCaller('caller message')

    print('Перехватывает ошибку')
    with caller.context_manager_intercept(RuntimeWarning) as cm_result:
        print(cm_result.lower())
        cm_result.raise_exception()

    print('Не возбуждает ошибку')
    with caller.context_manager_intercept() as cm_result:
        print(cm_result.upper())
        cm_result.raise_exception()

    print('Использует объект с поддержкой менеджера контекста без посредников')
    with ContextManagerObjectInterceptException('Direct context manager', RuntimeWarning) as cm_result:
        print(cm_result.msg)

    try:
        print('Пропустит ошибку выше (т. е. в данном случае её перехватит внешний обработчик)')
        with caller.context_manager_not_intercept(RuntimeError) as cm_result:
            cm_result.upper()
            cm_result.raise_exception()
    except Exception as err:
        print('Exception wrapper! Exception: {}'.format(repr(err)))
