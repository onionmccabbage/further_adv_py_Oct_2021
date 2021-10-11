# consider skills which need to be sought
# coder, tester, technician, artisan, manager

# all our classes are abstract with no inter-dependencies
class Coder():
    def __init__(self):
        print('Bring the coding skills')
    def __isAvailable__(self):
        print('coding skills are available')
        return True
    def bookTime(self):
        if self.__isAvailable__():
            print('coder has been booked')

class Tester():
    def __init__(self):
        print('Preparing tests')
    def testing(self):
        print('tests are in place')

class Technician():
    def __init__(self):
        print('Hardware and Networking for the team')
    def doStuff(self):
        print('Kit, network and virtual fridge are in place')

class Artisan():
    def __init__(self):
        print('Designing stuff')
    def makePrototype(self):
        print('Wireframes all done')

class Manager(): # facade to the team members
    def __init__(self):
        print('Manager says: I can arrange the team')
    def arrange(self):
        # we need isntances of the subsystems/microservices/pools
        self.tester = Tester()
        self.tester.testing()
        self.technician = Technician()
        self.technician.doStuff()
        self.coder = Coder()
        self.coder.bookTime()
        self.artisan = Artisan()
        self.artisan.makePrototype()

class You(): # you can be the client of this facade
    def __init__(self):
        print('we need a team....')
    def askManager(self):
        print('Lets contact the manager') # here we call the facade
        m = Manager()
        m.arrange()
    # del will be called in all classic Python flavours but carful with bundles e.g. Anaconda
    def __del__(self): 
        print('all done')

if __name__ == '__main__':
    you = You()
    you.askManager()