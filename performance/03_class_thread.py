from threading import Thread

class MyWorkerThread(Thread): # we inherit from the Thread class
    def __init__(self):
        print('This is an instance of our MyWorkerThread class')
        Thread.__init__(self) # call __init__ method of the Thread class
    # we override the default 'run' method of the Thread class
    def run(self): # this is the bit that gets called as a thread
        print('The thread is now running')

if __name__ == '__main__':
    myThread = MyWorkerThread()
    myThread.start() # this invokes the 'run' method
    myThread.join()
