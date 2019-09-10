# # Operator '+' is overloaded by both int and str classes
# print(5+6)
# print('a'+'b')
#
# print(int.__add__(5,6))
# print(str.__add__('a','b'))

# Overloading add method in a class
class Employee:

    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

    def __add__(self, other):
        sum = self.sal + other.sal
        return sum

    def __sub__(self, other):
        sub = self.sal - other.sal
        return sub

e1 = Employee('bhup',29000)
e2 = Employee('Rahul',23000)
print(type(e1), type(e2))
print(e1+e2)
print(e1-e2)
# print(Employee.__add__(e1,e2))
