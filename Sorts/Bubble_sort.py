def bubble_sort(collection):
    for i in range(len(collection)-1):              # i is the no. of loops remaining to be checked
        for j in range(len(collection)-1-i):        # j is the index of actual elements in the collection
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
            else:
                continue
    return collection


col = [2,5,3,8,6,9,1]
a = bubble_sort(col)
print(a)
