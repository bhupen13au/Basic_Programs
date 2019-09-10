# lst = [10,30,55,35,80,95,65]
# lst1 = [10,3,57,37,30,15,15]
#
# # print(sum(lst))
#
# res = 0
# for i in lst:
#     res += i
# print(res)

# print(max(lst))

# def smallno(lst):
#     m = lst[0]
#     for i in lst:
#         if i < m:
#             m = i
#         else:
#             m = m
#     print(m)
#
# smallno(lst1)

# Q: Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# lststr = ['abc', 'xyz', 'aba', '1221','abc', 'xyz', 'aba', '1221', 'a']
#
# def custom(lst):
#     count = 0
#     for i in lst:
#         if len(i)>=2 and i[0]==i[-1]:
#             count += 1
#     print(count)
#
# custom(lststr)

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# listTpl = [(2, 5,3), (1, 2,4), (4, 4,5), (2, 3,1), (2, 1,2)]
#
# for tpl in listTpl:
#     def middle(tpl):
#         return (tpl[1])
# print(sorted(listTpl,key=middle)) #sort by key where key is a function

# listOfWords = ['abds','dujhs','sghsas','dhsuj','shsu', 'aa','b']
# #
# # def findN(n):
# #     for i in listOfWords:
# #         if len(i)>n:
# #             print('These are the longer words', i)
# #
# # findN(4)

# list1 = []
# list2 = []
# n = 0
# while n <= 4:
#     i = input("Enter List 1:")
#     list1.append(i)
#     n += 1
# n = 0
# while n <= 4:
#     i = input("Enter List 2:")
#     list2.append(i)
#     n += 1
#
# for l1 in list1:
#     if l1 in list2:
#         print('True',l1)
#     continue
# print('False')

# lst = [i for i in range(10) if i % 2 == 0]
# print(lst)

# lst = {}
# counter = 0
# for i in range(10):
#     if i % 2 == 0:
#         lst[counter] = i
#         counter += 1
# print(lst)
count = 0
lst = {i:count+i for i, v in enumerate(range(10)) if v % 2 == 0}
print(lst)

# while True:
#     x = input('provide different types of brackets: ')
#
#     try:
#         y=eval(x)/0
#         print(y)
#         print('balanced')
#     except Exception as e:
#         print('Unbalanced',e,type(e))

# while True:
#     x = input('provide different types of brackets: ')
#     y = eval(x)
#     print(type(y),y)