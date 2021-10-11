# an exampel of the command design pattern
from abc import ABCMeta, AMCMeta, abstractmethod

# an abstract class
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade():
    pass

class Agent():
    pass

class BuyStock(Order):
    pass

class SellStock(Order):
    pass

if __name__ == '__main__':
    # client
    stock = StockTrade()
    # invoker
    agent = Agent()