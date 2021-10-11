# a proxy stands in for other things
# e.g. here are some payment methods and a bank
import random
from abc import ABC, ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self): # this is only available within this class
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print('Bank is checking if {} has sufficient funds'.format(self.__getAccount()))
        return bool(random.getrandbits(1)) # performant way to return True or False
    def setCard(self, card):
        self.card = card
    def do_pay(self):
        if self.__hasFunds():
            print('Bank i paying')
            return True
        else:
            print('Bank says not enough funds')
            return False
 
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input('Payment Proxy: Swipe, Tap or Insert card? ')
        self.bank.setCard(card)
        return self.bank.do_pay()
        
class You: # client
    def __init__(self):
        print('I need to buy a ...')
        self.debitCard = DebitCard()
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay() # call our proxy
    def __del__(self): # clean up
        if self.isPurchased:
            print('purchase went smoothly')
        else:
            print('anyone lend me a fiver?')



if __name__ == '__main__':
    you  = You() # client isntance
    you.makePayment() # try to use our proxy