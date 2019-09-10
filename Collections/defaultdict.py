from collections import defaultdict, UserDict
#
# d = defaultdict(int)
# d['aa'] = 11
# d['bb'] = 22
# # print(d)
# print(d['cc'])

dict_of_items = {'aa':11, 'bb':22, 'cc':33}
a = UserDict(dict_of_items)
print(a)
print(type(a))