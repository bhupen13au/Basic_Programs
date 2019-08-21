'''
def topTen():
    yield 5
    yield 10
    yield 15
    yield 'bhupen'

vals = topTen()

print(vals.__next__())
print(vals.__next__())
print(vals.__next__())
print(vals.__next__())
'''
'''
def topThree(list_of_scores):
    for i in list_of_scores:
        yield i

scores = [10,50,20,70,60,30,90,80]
tp = topThree(scores)

print(tp.__next__())
print(tp.__next__())
print(tp.__next__())
'''

def countdown(ip):
    num = ip
    yield num
    num -=1
    yield num*num   #Preserves the state
    num -= 1
    yield num/2
    num -= 1
    yield num+5
    num -= 1
    yield num

cd = countdown(10)
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
