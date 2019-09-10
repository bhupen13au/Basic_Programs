from collections import namedtuple

nTpl = namedtuple('course','subject,fees,duration,demand')

c1 = nTpl('Python',40000,'6 months', 'High')
print(c1)

c2 = nTpl('Java',35000,'7 months', 'Moderate')
print(c2)

c3 = nTpl._make(['C++',50000,'10 months','Low'])        #Using list
print(c3)
