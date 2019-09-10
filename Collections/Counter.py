from collections import Counter

lst = [1,2,3,2,2,1,3,4,7,6,4,5,8,9,9,8]

a = Counter(lst)

print(a)
print(type(a))
print(dict(a))
print(list(a.elements()))
print(a.most_common())

sub = {2:1,9:1}
a.subtract(sub)
print(a.most_common())