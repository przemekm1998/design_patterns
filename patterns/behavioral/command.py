from abc import ABCMeta, abstractmethod
from typing import List


class Order(metaclass=ABCMeta):
    """ The abstract command object """

    @abstractmethod
    def execute(self):
        pass


class StockTrade:
    """ Receiver """

    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")


class BuyStock(Order):
    """ Concrete command """

    def __init__(self, stock: StockTrade):
        self.stock: StockTrade = stock

    def execute(self):
        self.stock.buy()


class SellStock(Order):
    """ Concrete command """

    def __init__(self, stock: StockTrade):
        self.stock: StockTrade = stock

    def execute(self):
        self.stock.sell()


class Agent:
    """ Invoker """

    def __init__(self):
        self.__order_queue: List[Order] = list()

    def place_order(self, order: Order):
        self.__order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buy_stock = BuyStock(stock)
    sell_stock = SellStock(stock)

    # Invoker
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)
