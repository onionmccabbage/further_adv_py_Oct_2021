# we can get a memory profile to explore performance

# we may need to pip install -U memory_profiler
# to run: python -m memory_profiler do_profile.py

# we need to import the memory profiler
from memory_profiler import profile

import collections

def someFn():
    # here is a double ended queue
    my_deq = collections.deque('98765432')

    # we can alter members of the deque
    my_deq.append('1')
    my_deq.appendleft('0')
    my_deq.pop()
    my_deq.popleft()

    print('Dequeue {}'.format(my_deq))

@profile # we can decorate any function to get a memory profile
def main():
    someFn()

if __name__ == '__main__':
    main()