# we can accurately time code by using the timeit capabilities built in to Python
# the time module is good but timeit is more accurate
# timeit can ignore non-python time delays

import random
import time
import timeit

# we will use this to decorate any function we need to accurately time
def timethis(func):
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('The function {} took {} seconds to execute'.format(func.__name__, run_time))
        return value
    return function_timer

@timethis # we can decorate ANY function we need to time
def long_runner():
    for x in range(9):
        sleep_stime = random.choice(range(1,3))
        time.sleep(sleep_stime)

@timethis
def count_up():
    for i in range(1,10):
        x = 1

@timethis
def count_down():
    for j in range(10, 1, -1):
        y = 1


if __name__ == '__main__':
    long_runner()
    count_up()
    count_down()