import threading
import time
import random

# threads can be defined by functions which we call as threads
def threadWorker():
    print('the thread is running')
    time.sleep(2)
    print('the thread is terminating')

def executeThread(i): # we can pass in arguments
    print('Thread {} has started'.format(i))
    sleepTime = random.randint(1,4)
    time.sleep(sleepTime)
    print('Thread {} has finished executing'.format(i))

if __name__ == '__main__':
    # Thread is a thread-access object (not the thread itself)
    myThread = threading.Thread(target=threadWorker)
    myThread.start() # kick the thread into play (it starts running)
    # myThread.join() # optional, but a good idea
    # run several threads at once
    for i in range(0, 100, 10):
        # we can pass arguments as a tuple to a function being run on a thread
        thread = threading.Thread(target=executeThread, args=(i,))
        thread.start()
        print('Active Threads: {}'.format(threading.enumerate()))
        # thread.join() # this makes the threads sequential!
    # we could join all the threads here...then they remain parallel

    # best practice - make sure all threads are started before using join