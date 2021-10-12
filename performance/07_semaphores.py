# we have ticket sellers, each trying to sell tickets for a SINGLE show

import threading
import time
import random

class TicketSeller(threading.Thread): # we inherit from Thread
    ticketsSold = 0
    def __init__(self, sem):
        threading.Thread.__init__(self)
        self.__sem = sem
        print('Ticket seller started selling tickets')
    def run(self):
        global ticketsAvailable
        running = True # a flag
        while running:
            self.randomDelay()
            self.__sem.acquire() # we have access to the semaphore shared by all ticket sellers
            # are any tickets left?
            if (ticketsAvailable <= 0):
                running = False
            else:
                # lets sell those tickets
                self.ticketsSold += 1
                ticketsAvailable -= 1
                print('{} sold a ticket - {} remaining'.format(self.getName(), ticketsAvailable))
            self.__sem.release()
        # when the while loop ends, we're all done
        print('Ticket seller {} sold {} tickets'.format(self.getName(), self.ticketsSold))
    def randomDelay(self):
        time.sleep(random.randint(0 ,4)/4) # 0, 0.25, 0.5 or 0.75 seconds

if __name__ == '__main__':
    ticketsAvailable = 2*100000 # all ticket sellers will be selling these
    # we need a semaphore
    sem = threading.Semaphore(512) # how many can share this lock???
    # use this semaphore in our ticket seller instances
    sellers = [] # an empty list
    for i in range(1024):
        seller = TicketSeller(sem)
        seller.start()
        sellers.append(seller)
    for seller in sellers:
        seller.join() # once all the threads have started we can then call join on each one

# soe sample results
# Ticket seller Thread-3 sold 47 tickets
# Ticket seller Thread-4 sold 45 tickets
# Ticket seller Thread-2 sold 48 tickets
# Ticket seller Thread-1 sold 60 tickets

# Ticket seller Thread-2 sold 54 tickets
# Ticket seller Thread-3 sold 55 tickets
# Ticket seller Thread-4 sold 43 tickets
# Ticket seller Thread-1 sold 48 tickets

# Ticket seller Thread-1 sold 48 tickets
# Ticket seller Thread-4 sold 45 tickets
# Ticket seller Thread-2 sold 54 tickets
# Ticket seller Thread-3 sold 53 tickets