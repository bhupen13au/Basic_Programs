# def decorateor(fun):
#     print('*'*10)
#     fun()
#     print('*'*10)
#     return 'dec'
#
# @decorateor
# def newFun():
#     print('Hello brother')
#
# newFun

def decorator(fun):
    def fun2(num1,num2):
        if num1 < 0 and num2 < 0 :
            print('not valid')
        else:
            fun(num1,num2)
    return fun2

@decorator
def mult(num1,num2):
    result = num1 * num2
    return result

a = mult(7,5)
print(a)