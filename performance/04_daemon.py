import threading
import time

# NB for any threaded code, consider running with the -O flag
# the -O flag will optimize the byte-code for threading

def standardThread():
    print('starting a standard thread')
    time.sleep(8)
    print('ending standard thread')

def daemonThread(): # daemon keeps running until other threads end
    while True: # be very careful - make sure you can quit the loop!!
        print('heartbeat....')
        time.sleep(2)

if __name__ == '__main__':
    stan = threading.Thread(target=standardThread)
    daem = threading.Thread(target=daemonThread)
    # we can set a thread to act as a Daemon thread
    daem.setDaemon(True)
    daem.start()
    stan.start()

    # no join....