# lst = [1,[2,[3,[4,[5]]]]]
#
# f_list = []
# for i in lst:
#     if type(i)==int:
#         f_list.append(i)
#     elif type(i)==list:
#         for j in i:
#             if type(j)==int:
#                 f_list.append(j)
#             else:
#                 i = j
#
# print(f_list)

lst = [10,12,[12,66,[33,88,[54,99,[15,9]]]]]
#
# f_list = []
# x = lst
# for k in range(5):
#     for j in range(len(x)):
#         if type(x[j]) == int:
#             f_list.append(x[j])
#         else:
#             x = x[j]
#
# print(f_list)
