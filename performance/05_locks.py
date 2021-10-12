import threading
import time

# this module declares some globals
counter = 1
lock = threading.Lock()

def workerA():
    global counter
    lock.acquire()
    try:
        while counter <100:
            counter += 1 # increment
            print('Worker A increments counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release()
        pass

def workerB():
    global counter
    lock.acquire()
    try:
        while counter >-100:
            counter -= 1 # decrement
            print('Worker B decrements counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release()
        pass

if __name__ == '__main__':
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    # Execution took 0.0029861927032470703 seconds with lock
    # Execution took 0.050998687744140625 seconds wihout lock
    # even quicker with no print statements!!
    print('Execution took {} seconds'.format(t1-t0))