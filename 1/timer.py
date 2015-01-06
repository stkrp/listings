"""
Lutz

Добавить элемент в начало списка
(тесты разных решений)
"""

import time


class Timer(object):
    """
    Исследовать функцию по времени выполнения
    """

    def __init__(self, func, *pargs, **kwargs):
        self.func = func
        self.pargs = pargs
        self.kwargs = kwargs

    def run_distributed(self, *, replays=1000, assign_value=True, per_replay=False):
        """
        Замерить среднюю скорость выполнения функции
        :param replays: количество повторов
        :param assign_value: запоминать возвращаемое значение или нет
        :param per_replay: хранить ли время каждого повторения или нет
        :return:
        """

        replays_list = range(replays)
        replays_duration_list = []

        if per_replay:
            if assign_value:
                for replay in replays_list:
                    start = time.clock()
                    value = self.func(*self.pargs, **self.kwargs)
                    replays_duration_list.append(time.clock() - start)
            else:
                for replay in replays_list:
                    start = time.clock()
                    self.func(*self.pargs, **self.kwargs)
                    replays_duration_list.append(time.clock() - start)
            duration = sum(replays_duration_list)
        else:
            if assign_value:
                start = time.clock()
                for replay in replays_list:
                    value = self.func(*self.pargs, **self.kwargs)
            else:
                start = time.clock()
                for replay in replays_list:
                    self.func(*self.pargs, **self.kwargs)
            duration = time.clock() - start

        avg_duration = duration / replays

        result = {
            'replays': replays,
            'duration': duration,
            'avg_duration': avg_duration
        }

        if per_replay:
            result['replays_duration_list'] = replays_duration_list

        return result

    def run_solid(self, *, replays=1000, assign_value=True, per_replay=False):
        """
        Замерить среднюю скорость выполнения функции
        :param replays: количество повторов
        :param assign_value: запоминать возвращаемое значение или нет
        :param per_replay: хранить ли время каждого повторения или нет
        :return:
        """

        replays_list = range(replays)
        replays_duration_list = []

        start = time.clock()
        for replay in replays_list:
            if assign_value:
                returned_value = self.func(*self.pargs, **self.kwargs)
            else:
                self.func(*self.pargs, **self.kwargs)
            if per_replay:
                replay_duration = time.clock() - start
                replays_duration_list.append(replay_duration)
                start = time.clock()
        end = time.clock()

        duration = sum(replays_duration_list) if per_replay else end - start
        avg_duration = duration / replays

        result = {
            'replays': replays,
            'duration': duration,
            'avg_duration': avg_duration
        }

        if per_replay:
            result['replays_duration_list'] = replays_duration_list

        return result

if __name__ == '__main__':
    test_params = (sum, [12, 123, 32345] * 12345)
    print(Timer(*test_params).run_distributed(assign_value=False, per_replay=False))
    print(Timer(*test_params).run_distributed(assign_value=False, per_replay=True))
    print(Timer(*test_params).run_distributed(assign_value=True, per_replay=False))
    print(Timer(*test_params).run_distributed(assign_value=True, per_replay=True))
    print(Timer(*test_params).run_solid(assign_value=False, per_replay=False))
    print(Timer(*test_params).run_solid(assign_value=False, per_replay=True))
    print(Timer(*test_params).run_solid(assign_value=True, per_replay=False))
    print(Timer(*test_params).run_solid(assign_value=True, per_replay=True))