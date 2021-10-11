# consider a laptop which can be in one of ON, OFF, SLEEP or HYBERNATE states
# we can go from OFF to ON, ON to SLEEP but not OFF to SLEEP

class ComputerState:
    name = 'state'
    allowed = [] # this list will contain permitted states to change to
    def switch(self, state):
        if state.name in self.allowed:
            print('Current state {} switching to {}'.format(self, state.name ))
            self.__class__ = state # make the switch
        else:
            print('Current state {} cannot switch to {}'.format(self, state.name))
    def __str__(self):
        return self.name

class On(ComputerState):
    name = 'on'
    allowed = ['off', 'sleep', 'hybernate']

class Off(ComputerState):
    name = 'off'
    allowed = ['on']

class Sleep(ComputerState):
    name = 'sleep'
    allowed = ['on']
    
class Hybernate(ComputerState):
    name = 'hybernate'
    allowed = ['on']

class Computer():
    def __init__(self, computer_model):
        self.model = computer_model
        self.state = Off() # initial state for all computers when they are instatiated
    def change(self, change_to): # pass in the state we want to change to
        self.state.switch(change_to)

if __name__ == '__main__':
    comp = Computer('Laptop') # initially in state 'off'
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Sleep)
    comp.change(On)
    comp.change(Hybernate)
    comp.change(On)
    comp.change(Sleep)
    comp.change(Hybernate) # nope - this state change is not permitted