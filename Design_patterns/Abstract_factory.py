from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_product1(self):
        pass

    @abstractmethod
    def create_product2(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product1(self):
        return Product1_1()

    def create_product2(self):
        return Product2_1()


class ConcreteFactory2(AbstractFactory):
    def create_product1(self):
        return Product1_2()

    def create_product2(self):
        return Product2_2()


class AbstractProduct1(ABC):

    @abstractmethod
    def display(self):
        pass


class Product1_1():
    def display(self):
        print("Inside product1_1 display")


class Product1_2():
    def display(self):
        print("Inside product1_2 display")


class AbstractProduct2(ABC):

    @abstractmethod
    def display(self):
        pass


class Product2_1():
    def display(self):
        print("Inside product2_1 display")


class Product2_2():
    def display(self):
        print("Inside product2_2 display")


factory1 = ConcreteFactory1()
product1 = factory1.create_product1()
product1.display()

product2 = factory1.create_product2()
product2.display()

factory2 = ConcreteFactory2()
product1 = factory2.create_product1()
product1.display()

product2 = factory2.create_product2()
product2.display()