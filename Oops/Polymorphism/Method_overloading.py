# # Method overloading not possible
# class Sum:
#     result = 0
#
#     def add(self,num1):
#         self.result = num1
#         return self.result
#
#     def add(self,num1,num2):
#         self.result = num1 + num2
#         return self.result
#
#     def add(self,num1,num2,num3):
#         self.result = num1 + num2 + num3
#         return self.result
#
# s = Sum()
# # print(s.add(7,6,5))
#
#
# # Method overloading made possible
# class Sum:
#     result = 0
#
#     def add(self,num1=None,num2=None,num3=None):
#         if num1 != None and num2 != None and num3 != None :
#             self.result = num1 + num2 + num3
#             return self.result
#         elif num1 != None and num2 != None and num3 == None :
#             self.result = num1 + num2
#             return self.result
#         elif num1 != None and num2 == None and num3 == None :
#             self.result = num1
#             return self.result
#
# s = Sum()
# print(s.add(7,6,5))
# print(s.add(6,5))
# print(s.add(7))

class Sum:


    def add(self, *args):
        result = 0
        for i in args:
            result = result+i
        return result

s = Sum()
print(s.add(7,6,5,7,6,5))
print(s.add(6,5))
print(s.add(7))