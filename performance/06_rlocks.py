# using re-entrant locks (rlocks)
import threading
import time

# we may use functions or classes for our threads
class MyWorker(): # NB this class does NOT inherit from Thread...
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # a re-entrant lock
    def modifyA(self):
        with self.rlock: # using 'with' will automatically release the lock when done
            print('RLock acquired {}, modifying A'.format( self.rlock.__is_owned() ))
            # take a look at the RLock itself
            print('{}'.format(self.rlock))
            self.a += 1
            time.sleep(2)
    def modifyB(self):
        with self.rlock: # using 'with' will automatically release the lock when done
            print('RLock acquired {}, modifying B'.format( self.rlock.__is_owned() ))
            # take a look at the RLock itself
            print('{}'.format(self.rlock))
            self.b -= 1
            time.sleep(2)
    def modifyBoth(self):
        with self.rlock: # using 'with' will automatically release the lock when done
            print('RLock acquired {}, modifying A and B'.format( self.rlock.__is_owned() ))
            # take a look at the RLock itself
            self.modifyA()
            print('{}'.format(self.rlock))
            self.modifyB()
            print('{}'.format(self.rlock))
        print('{}'.format(self.rlock)) # this line is after the 'with' ends

if __name__ == '__main__':
    worker = MyWorker()
    worker.modifyBoth()
    worker.modifyA()