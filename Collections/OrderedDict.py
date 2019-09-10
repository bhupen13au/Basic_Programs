from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)

print(od.keys())
print(od.items())
print(od.get('c'))
od['b'] = 20
print(od)

dicto = {'aa':1,'bb':2,'cc':3,'dd':4}
print(dicto)
dicto['bb'] = 20
print(dicto)
