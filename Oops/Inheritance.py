# Single Inheritance
# x=0
# class fruit:
#     def __init__(self):
#         global x
#         x+=1
#         print("I'm a fruit")
# class citrus(fruit):
#     def __init__(self):
#         super().__init__()
#         global x
#         x+=2
#         print("I'm citrus")
#
# print(x)
# ctr = citrus()
# print(ctr)
# print(x)


# Multiple Inheritance
# class Color:
#     pass
# class Fruit:
#     pass
# class Orange(Color,Fruit):
#     pass
# a = issubclass(Orange,Color) and issubclass(Orange,Fruit)
# print(a)


# Multilevel Inheritance
# class A:
#     x=1
# class B(A):
#     pass
# class C(B):
#     pass
# cobj=C()
# print(cobj.x)


# Hierarchical Inheritance
# class A:
#     x = 1
# class B(A):
#     x = 2
# class C(A):
#     z = 3
# a = issubclass(B,A) and issubclass(C,A)
# print(a)
# c = C()
# print(c.x)


# Hybrid Inheritance
class A:
    x=1
class B(A):
    y=2
class C(A):
    x=3
class D(B,C):
    pass
dobj=D()
print(dobj.x)
