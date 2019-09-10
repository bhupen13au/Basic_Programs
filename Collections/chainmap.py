from collections import ChainMap

A = {1:'Bhupendra', 2:'Rahul'}
B = {3:'Shivraj', 4:'Bivek'}
C = {5:'JayShree', 6:'Mamta'}

c1 = ChainMap(A,B,C)
print(c1)
