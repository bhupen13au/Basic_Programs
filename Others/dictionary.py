oldDict = {1:5, 3:1, 5:4, 7:3, 9:2}


for dct in oldDict:
    def keys(dct):
        return (dct[1])
print(sorted(oldDict,key=keys))

# newDict = {}

# for d in oldDict:
# #     print(oldDict.values())
# #     print(d)

# k = oldDict.keys()
# kl = list(k)
# print(kl)
# for ky in kl:
#
#     print(oldDict[ky])

