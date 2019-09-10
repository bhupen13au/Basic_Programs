class Myclass:
    def f(self):
        print('this is function f')

def monkey_f(self):
    print('this is function monkey_f')

Myclass.f = monkey_f
obj = Myclass()
obj.f()