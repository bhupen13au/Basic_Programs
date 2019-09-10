from abc import ABC, abstractmethod

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class ConcreteClass1(Prototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
        self.i,
        self.s,
        self.l.copy(),
        self.d.copy()
        )

    def __str__(self):
        return str(self.__dict__)


class ConcreteClass2(Prototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy()
        )

    def __str__(self):
        return str(self.__dict__)


object1 = ConcreteClass1(1,"OBJECT1",[1,2,3,4],{'a':1,'b':2,'c':3,'d':4})
print(object1)

object2 = object1.clone()
print(object2)
