import multiprocessing

def myProcFn():
    # every process has it's own copy of Python
    print('Executing a child process on a separate processor - with its own GIL')

if __name__ == '__main__':
    print('Here is the main proces')
    myOtherProcA = multiprocessing.Process(target=myProcFn)
    myOtherProcA.start()
    myOtherProcA.join()
    myOtherProcB = multiprocessing.Process(target=myProcFn)
    myOtherProcB.start()
    myOtherProcB.join()
    myOtherProcC = multiprocessing.Process(target=myProcFn)
    myOtherProcC.start()
    myOtherProcC.join()
    print('child process has terminated')