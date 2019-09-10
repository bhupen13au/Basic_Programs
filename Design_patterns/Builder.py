from abc import ABC, abstractmethod


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builderObj):
        self.builder = builderObj

    def construct(self, name):
        if name == 'Product1':
            self.builder.create()
            self.builder.build_part_A()
            self.builder.build_part_B()
        elif name == 'Product2':
            self.builder.create()
            self.builder.build_part_C()
            self.builder.build_part_D()

class Builder(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def build_part_A(self):
        pass

    @abstractmethod
    def build_part_B(self):
        pass

    @abstractmethod
    def build_part_C(self):
        pass

    @abstractmethod
    def build_part_D(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = None

    def create(self):
        self.product = product1()

    def build_part_A(self):
        pass

    def build_part_B(self):
        pass

    def build_part_C(self):
        pass

    def build_part_D(self):
        pass

    def get_product(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = None

    def create(self):
        self.product = product2()

    def build_part_A(self):
        pass

    def build_part_B(self):
        pass

    def build_part_C(self):
        pass

    def build_part_D(self):
        pass

    def get_product(self):
        return self.product


class product1:
    def display(self):
        print('Inside product1')

class product2:
    def display(self):
        print('Inside product2')


director = Director()

builder1 = ConcreteBuilder1()
director.set_builder(builder1)
director.construct('Product1')
prod1 = builder1.get_product()
prod1.display()

builder2 = ConcreteBuilder2()
director.set_builder(builder2)
director.construct('Product2')
prod2 = builder2.get_product()
prod2.display()