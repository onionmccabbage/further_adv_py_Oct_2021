# an exampel of the command design pattern
from abc import ABCMeta, abstractmethod

# an abstract class
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade():
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class Agent():
    def __init__(self):
        self.__orderQueue = [] # we start with an empty list
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() # in this case, the order is immediately execited
        # but we could wait until available resources before executing

# concrete classes derived form abstract 'Order' class
class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.sell()

if __name__ == '__main__':
    # client
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    # invoker
    agent = Agent()
    # we can now invoke the commands to buy or sell
    agent.placeOrder(buy)
    agent.placeOrder(sell)