class Singleton(object):
    instance = None
    print(instance,'class level instance')

    @classmethod
    def instance_cls(cls):
        print('class method first')
        if cls.instance == None:
            print('class method')
            cls.instance = Singleton()
        return cls.instance

    def __init__(self):
        print('init constructor')
        if self.instance != None:
            print('Constructor')
            raise ValueError("A Singleton instance already exists")

    def set_data(self, num):
        self.data = num

    def get_data(self):
        return self.data

obj = Singleton()
obj.set_data(10)
print(obj.get_data())

# obj1 = Singleton()
# obj1.set_data(20)
# print(obj1.get_data())
#
