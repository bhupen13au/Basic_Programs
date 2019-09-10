# import re
#
# msg = '''Rahul is 29 and Satish is 30
#         Amol is 34 and Shivraj is 25'''
#
# ages = re.findall(r'\d{1,3}', msg)
# names = re.findall(r'[A-Z][a-z]*', msg)
#
# age_dict = {}
#
# for nm in names:
#     i=0
#     age_dict[nm] = ages[i]
#     i+=1
#
# print(age_dict)


# import re
#
# msg = '''We need to inform him with the latest information'''
#
# if re.search('inform',msg):
#     print('present')
# else:
#     print('not present')


# import re
#
# msg = '''We need to inform him with the latest information'''
#
# finder = re.finditer('inform',msg)
#
# for i in finder:
#     print(i.span())


# import re
#
# str = 'Sat, hat, mat, pat, rat'
#
# all_str = re.findall(r'[Shrpm]at',str)
#
# for i in all_str:
#     print(i)


# import re
#
# str = 'Sat, hat, mat, pat, rat'
#
# comp = re.compile("[m]at")
# food = comp.sub("food",str)
#
# print(food)


# import re
#
# str = '9977645500'
# print('Matches', len(re.findall('\d{5}',str)))


# import re
#
# phn = '989-543-1234'
#
# if re.search('\d{3}-\d{3}-\d{4}',phn):
#     print('valid phone no.')
# else:
#     print('Invalid phone no.')


