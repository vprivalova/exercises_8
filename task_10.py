import time
import functools


def runtime_restriction(runtime, n, seconds):
    def decorator(func):
        timing = []
        counter = 0

        @functools.wraps(func)
        def wrapped(num):
            nonlocal counter
            nonlocal timing
            current = time.time()
            timing.append(current)

            if current - timing[0] <= seconds:
                counter += 1

            if counter > n:
                raise Exception('Function was called too many times ')

            start = time.time()
            result = func(num)
            end = time.time()
            overall_time = end - start
            if overall_time > runtime:
                raise RuntimeError('Too much time is taken')
            else:
                return result
        return wrapped
    return decorator


@runtime_restriction(1, 4, 20)
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


print(factorial(144))
print(factorial(3))
print(factorial(9))
print(factorial(8))
print(factorial(1))
