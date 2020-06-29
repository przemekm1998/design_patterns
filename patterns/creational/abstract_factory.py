from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_meat_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_meat_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_meat_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class MeatPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('prepare ', type(self).__name__)


class ChickenPizza(MeatPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, " is served with Chicken on ",
              type(veg_pizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(MeatPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
        self.factory = factory
        self.NonVegPizza = self.factory.createNonVegPizza()
        self.VegPizza = self.factory.createVegPizza()
        self.VegPizza.prepare()
        self.NonVegPizza.serve(self.VegPizza)