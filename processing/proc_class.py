import multiprocessing
import os
# declare a class which inherits from Process
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    # we override the default run method
    def run(self):
        print('Child Process ID is {}'.format( multiprocessing.current_process().pid ))

def main():
    print('Main process ID is {}'.format( multiprocessing.current_process().pid ))
    myProc = MyProcess()
    myProc.start()
    myProc.join() 
    # we can spawn a bunch of processes
    processes = []
    for i in range(os.cpu_count()): # e.g. 16
        p = MyProcess()
        processes.append(p)
        p.start()
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    main()