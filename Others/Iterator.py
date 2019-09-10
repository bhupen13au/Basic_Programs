#
# list_of_num = [10,50,20,70,60,30,90,80]
#
# it = iter(list_of_num)
# print(it)
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# #or
# print(next(it))
# print(next(it))


class TopThree:

    def __init__(self,list_of_scores):
        self.index = 0
        self.lst = list_of_scores

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <3:
            val = self.lst[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

# scores = [10,50,20,70,60,30,90,80]
# tp = TopThree(scores)
#
# # for i in tp:
# #     print(i)
#
# print(next(tp))
# print(next(tp))
# print(next(tp))
# # print(next(tp))

tps = TopThree('bhupendra')

# for i in tps:
#     print(i)

print(next(tps))
print(next(tps))
print(next(tps))
