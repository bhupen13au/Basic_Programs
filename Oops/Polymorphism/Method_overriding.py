class A:
    def m1(self):
        print('insde m1_A')

class B(A):
    def m1(self):
        print('inside m1_B')
        super().m1()
    def m2(self):
        print('inside m2_B')

b = B()
b.m1()
# b.m2()
